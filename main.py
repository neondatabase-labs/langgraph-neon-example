import os

import psycopg2
from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage
from langgraph.prebuilt import create_react_agent
from neon_api import NeonAPI
from psycopg2.extras import RealDictCursor

load_dotenv()

neon_client = NeonAPI(
    api_key=os.environ["NEON_API_KEY"],
)


@tool
def create_database(project_name: str) -> str:
    """
    Creates a new Neon project. (this takes less than 500ms)
    Args:
        project_name: Name of the project to create
    Returns:
        the connection URI for the new project
    """
    try:
        project = neon_client.project_create(project={"name": project_name}).project
        connection_uri = neon_client.connection_uri(
            project_id=project.id, database_name="neondb", role_name="neondb_owner"
        ).uri

        return f"Project/database created, connection URI: {connection_uri}"
    except Exception as e:
        return f"Failed to create project: {str(e)}"


@tool
def run_sql_query(connection_uri: str, query: str) -> str:
    """
    Runs an SQL query in the Neon database.
    Args:
        connection_uri: The connection URI for the Neon database
        query: The SQL query to execute
    Returns:
        the result of the SQL query
    """
    conn = psycopg2.connect(connection_uri)
    cur = conn.cursor(cursor_factory=RealDictCursor)
    try:
        cur.execute(query)
        conn.commit()
        try:
            records = cur.fetchall()
            return f"Query result: {records}"
        except psycopg2.ProgrammingError:
            return f"Query executed successfully"
    except Exception as e:
        conn.rollback()
        return f"Failed to execute SQL query: {str(e)}"
    finally:
        cur.close()
        conn.close()


available_tools = [create_database, run_sql_query]

system_prompt = SystemMessage(
    f"You are a helpful AI assistant. You will be assisting users with all of your available tools. You can help users by using the following tools: {', '.join([f"\n{tool.name}: {tool.description}" for tool in available_tools])}."
)

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")
agent_graph = create_react_agent(
    model=model,
    tools=available_tools,
    prompt=system_prompt,
)

inputs = {
    "messages": [
        (
            "user",
            "Create a new Neon project called langgraph and create a table named users. Add 10 sample records to the table. Then print the records as a markdown table.",
        )
    ]
}
result = agent_graph.invoke(inputs)

print("Step by Step execution : ")
for message in result["messages"]:
    print(message.pretty_repr())

with open("graph.png", "wb") as f:
    f.write(agent_graph.get_graph().draw_mermaid_png())