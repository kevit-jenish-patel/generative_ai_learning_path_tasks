
# RAG Task

Implemented Retrieval Argumented Generation Pipeline to build a chatbot that answers user queries from data extracted from documents.
## Features

- **Interactive Chat Interface**: Streamlit-based UI for real-time chat interactions.
- **RAG-powered Responses**: Retrieves relevant information and generates intelligent responses using a knowledge pipeline.
- **Chat History**: Maintains conversation history across interactions.
- **Streaming Responses**: Simulates typing effect for assistant responses.
- **Data Ingestion Pipeline**: Prepares and ingests data automatically for the assistant to use.
- **Clear Chat Functionality**: Reset the conversation with a single button click.


## Tech Stack

- **Groq llama-3.3-70b-versatile**: The language model for code generation.

- **LiteLLM**: For integrating the llm model.

- **Langfuse**: For monitoring and tracing the llm requests.

- **Streamlit**: For building the interactive web application.


## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`GROK_API_KEY`

`LANGFUSE_PUBLIC_KEY`

`LANGFUSE_SECRET_KEY`

`LANGFUSE_HOST`


## Run application

Clone the project

```bash
  git clone https://github.com/kevit-jenish-patel/generative_ai_learning_path_tasks.git
```

Go to the project directory

```bash
  cd RAGTask
```

Install dependencies from requirements.txt

```bash
  pip install -r requirements.txt
```

Start the application

```bash
  streamlit run apps/__main__.py
```

## Authors

- [@jenish](https://www.github.com/kevit-jenish-patel)

