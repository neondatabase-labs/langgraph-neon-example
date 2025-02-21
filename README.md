<img width="250px" src="https://neon.tech/brand/neon-logo-dark-color.svg" />

# LangGraph + Neon example

**A step-by-step example guide to building AI Agents using LangGraph and Neon**

This repository accompanies the guide [**Getting started with LangGraph + Neon**](https://neon.tech/guides/langgraph-neon). It provides a practical example of how to integrate [LangGraph](https://www.langchain.com/langgraph), a framework for building stateful AI agent workflows, with [Neon](https://neon.tech/), a serverless Postgres platform.

In this example guide, you'll learn how to build a simple [ReAct agent](https://arxiv.org/abs/2210.03629) using LangGraph that can interact with your Neon database to automate database management tasks, such as creating Neon projects and executing SQL queries. It builds upon the concepts demonstrated in the [prebuilt ReAct agent from LangGraph](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent).

## ✨ What you will build

This example will show you how to:

- **Set up a LangGraph ReAct agent:** Create and configure a ReAct agent using LangGraph's `create_react_agent`.
- **Integrate LangGraph with Neon API:** Use Python functions as tools for your agent to interact with Neon for database operations.
- **Automate Neon database management:** Enable your AI agent to create Neon projects and execute SQL queries using natural language commands.
- **Implement a ReAct workflow:** Understand the Reason and Act pattern within a LangGraph agent for iterative problem-solving.
- **Observe step-by-step agent execution:** See how LangGraph provides detailed logs of the agent's reasoning and actions.

## 🚀 Get started

You can run this example on your local machine or in a cloud-based development environment using [GitHub Codespaces](https://github.com/features/codespaces).

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/neondatabase-labs/langgraph-neon-example)

### Prerequisites

Before you begin, make sure you have the following:

1.  **Python 3.10 or higher:**  Ensure you have Python 3.10 or a later version installed. Download from [python.org](https://www.python.org/downloads/).
2.  **Neon Account and API Key:**
    - Sign up for a free Neon account at [neon.tech](https://console.neon.tech/signup).
    - Obtain your Neon API Key from the [Neon console](https://console.neon.tech/app/settings/profile).
3.  **Google API Key:**
    - You'll need a Google API key to proceed. If you don't already have one, get an API key from the [Google AI Studio](https://aistudio.google.com/apikey).
    - The free tier is sufficient for the example in this guide.

### Installation and setup

1.  **Clone this repository:**

    ```bash
    git clone https://github.com/neondatabase-labs/langgraph-neon-example
    cd langgraph-neon-example
    ```

2.  **Set up a virtual environment:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # For Windows: venv\Scripts\activate
    ```

3.  **Install required libraries:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure API keys:**

    - Copy the example environment file:

      ```bash
      cp .env.example .env  # On Linux/macOS
      ```

    - Open the `.env` file and fill in your API keys:

      ```env
      GOOGLE_API_KEY=YOUR_GOOGLE_API_KEY
      NEON_API_KEY=YOUR_NEON_API_KEY
      ```

      **Replace the placeholders** with your actual API keys obtained from Google AI Studio and Neon.

### Run the example

Now you're ready to run the LangGraph agent example!

```bash
python main.py
```

This command will execute the `main.py` script, which:

- Creates a LangGraph ReAct agent powered by Google's Gemini model.
- Provides the agent with tools to create Neon projects and run SQL queries.
- Instructs the agent to create a Neon project, create a table, insert records, and print the records as a markdown table based on user input.
- Prints the step-by-step execution and results to your console.

**Expected Output:**

You'll see a detailed execution of the LangGraph agent in your terminal, demonstrating how it reasons and uses tools to interact with Neon. The output will showcase the agent creating a Neon project, executing SQL queries, and formatting the results.

Here's the entire conversation log showing the step-by-step execution of the agent:

```text
Step by Step execution : 
================================ Human Message =================================

Create a new Neon project called langgraph and create a table named users. Add 10 sample records to the table. Then print the records as a markdown table.
================================== Ai Message ==================================

I can create a Neon project and a table named users, and add 10 sample records to the table. However, I cannot automatically print the records as a markdown table. I will need to run a query to fetch the records first, and then you can format them as a markdown table.

First, I will create the project:
Tool Calls:
  create_database (b9e5d9f7-5b8c-40f0-af6c-7ec095ba2da9)
 Call ID: b9e5d9f7-5b8c-40f0-af6c-7ec095ba2da9
  Args:
    project_name: langgraph
================================= Tool Message =================================
Name: create_database

Project/database created, connection URI: postgresql://neondb_owner:npg_HCFnoIvx5L9g@ep-broad-water-a53lox4z.us-east-2.aws.neon.tech/neondb?sslmode=require
================================== Ai Message ==================================

OK. I've created the project and the connection URI is postgresql://neondb_owner:npg_HCFnoIvx5L9g@ep-broad-water-a53lox4z.us-east-2.aws.neon.tech/neondb?sslmode=require. Now, I will create the table and add the records.
Tool Calls:
  run_sql_query (c3346333-b024-4fc5-99ba-d745e0108bb8)
 Call ID: c3346333-b024-4fc5-99ba-d745e0108bb8
  Args:
    connection_uri: postgresql://neondb_owner:npg_HCFnoIvx5L9g@ep-broad-water-a53lox4z.us-east-2.aws.neon.tech/neondb?sslmode=require
    query: CREATE TABLE users (id INT PRIMARY KEY, name VARCHAR(255), email VARCHAR(255));
================================= Tool Message =================================
Name: run_sql_query

Query executed successfully
================================== Ai Message ==================================
Tool Calls:
  run_sql_query (4be2ae12-adfe-45ed-bba3-d321073902ef)
 Call ID: 4be2ae12-adfe-45ed-bba3-d321073902ef
  Args:
    connection_uri: postgresql://neondb_owner:npg_HCFnoIvx5L9g@ep-broad-water-a53lox4z.us-east-2.aws.neon.tech/neondb?sslmode=require
    query: INSERT INTO users (id, name, email) VALUES (1, 'John Doe', 'john.doe@example.com'), (2, 'Jane Smith', 'jane.smith@example.com'), (3, 'Robert Jones', 'robert.jones@example.com'), (4, 'Emily Brown', 'emily.brown@example.com'), (5, 'Michael Davis', 'michael.davis@example.com'), (6, 'Jessica Wilson', 'jessica.wilson@example.com'), (7, 'Christopher Garcia', 'christopher.garcia@example.com'), (8, 'Ashley Rodriguez', 'ashley.rodriguez@example.com'), (9, 'Matthew Williams', 'matthew.williams@example.com'), (10, 'Brittany Miller', 'brittany.miller@example.com');
================================= Tool Message =================================
Name: run_sql_query

Query executed successfully
================================== Ai Message ==================================
Tool Calls:
  run_sql_query (f6484943-0dcc-4059-b794-2dc83ae31b1a)
 Call ID: f6484943-0dcc-4059-b794-2dc83ae31b1a
  Args:
    connection_uri: postgresql://neondb_owner:npg_HCFnoIvx5L9g@ep-broad-water-a53lox4z.us-east-2.aws.neon.tech/neondb?sslmode=require
    query: SELECT * FROM users;
================================= Tool Message =================================
Name: run_sql_query

Query result: [RealDictRow({'id': 1, 'name': 'John Doe', 'email': 'john.doe@example.com'}), RealDictRow({'id': 2, 'name': 'Jane Smith', 'email': 'jane.smith@example.com'}), RealDictRow({'id': 3, 'name': 'Robert Jones', 'email': 'robert.jones@example.com'}), RealDictRow({'id': 4, 'name': 'Emily Brown', 'email': 'emily.brown@example.com'}), RealDictRow({'id': 5, 'name': 'Michael Davis', 'email': 'michael.davis@example.com'}), RealDictRow({'id': 6, 'name': 'Jessica Wilson', 'email': 'jessica.wilson@example.com'}), RealDictRow({'id': 7, 'name': 'Christopher Garcia', 'email': 'christopher.garcia@example.com'}), RealDictRow({'id': 8, 'name': 'Ashley Rodriguez', 'email': 'ashley.rodriguez@example.com'}), RealDictRow({'id': 9, 'name': 'Matthew Williams', 'email': 'matthew.williams@example.com'}), RealDictRow({'id': 10, 'name': 'Brittany Miller', 'email': 'brittany.miller@example.com'})]
================================== Ai Message ==================================

| id | name               | email                        |
| -- | ------------------ | ---------------------------- |
| 1  | John Doe           | john.doe@example.com         |
| 2  | Jane Smith          | jane.smith@example.com        |
| 3  | Robert Jones        | robert.jones@example.com       |
| 4  | Emily Brown         | emily.brown@example.com        |
| 5  | Michael Davis       | michael.davis@example.com      |
| 6  | Jessica Wilson      | jessica.wilson@example.com     |
| 7  | Christopher Garcia  | christopher.garcia@example.com |
| 8  | Ashley Rodriguez    | ashley.rodriguez@example.com   |
| 9  | Matthew Williams    | matthew.williams@example.com   |
| 10 | Brittany Miller     | brittany.miller@example.com    |
```

### Visualizing the Agent Graph (Optional)

To better understand the structure of your LangGraph agent, you can visualize the execution graph directly within the code. Add the following lines at the end of your `main.py` script:

```python
with open("graph.png", "wb") as f:
    f.write(agent_graph.get_graph().draw_mermaid_png())
```

This will generate a `graph.png` file in your project directory, visualizing the agent's workflow.

![LangGraph Agent Graph](./graph.png)

**Understanding the Graph:**

The graph visualization provides a clear representation of your agent's workflow, showing the flow of execution between different components:

- **Nodes:** Represented as rounded boxes, each node signifies a step in the agent's process. In this example, you'll see nodes for `__start__`, `agent`, `tools`, and `__end__`.
- **Edges:** Arrows connecting the nodes illustrate the flow of execution. Solid lines typically indicate sequential flow, while dotted lines often represent conditional or tool-use paths.

By examining the graph, you can quickly grasp the overall structure of your LangGraph agent, understand the sequence of operations, and identify decision points and tool integrations.

## Resources

- [LangGraph Github](https://github.com/langchain-ai/langgraph)
- [LangGraph Documentation](https://python.langchain.com/docs/langgraph)
- [LangGraph Conceptual Guide](https://langchain-ai.github.io/langgraph/concepts)
- [Neon Documentation](https://neon.tech/docs)
- [Neon API reference](https://api-docs.neon.tech/reference/getting-started-with-neon-api)
- [Neon API keys](https://neon.tech/docs/manage/api-keys#creating-api-keys)

## 🤝 Contributing

Contributions are welcome! If you have suggestions for improvements or find any issues, please feel free to open an issue or submit a pull request.
