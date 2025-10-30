
# Amazon Rainforest Assistant

An LLM based chatbot that answers user queries regarding the Amazon Rainforest.

## Features

- Dynamic context through scrapping
- Accurate LLM responses
- Beautiful responsive UI
- Response streaming

## Tech Stack

**UI:** Streamlit

**Scrapping:** Requests , BeautifulSoup

**LLM Provider:** OpenAI

**LLM Model:** gpt-4.1-nano

**Monitorig:** Langfuse

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

Inside the microservices/auth/.env file

`MONGODB_URI`

`LANGFUSE_SECRET_KEY`

`LANGFUSE_PUBLIC_KEY`

`LANGFUSE_BASE_URL`

`WEBSITE_URL_TO_SCRAP`

`OPENAI_API_KEY`

`OPENAI_ASSISTANT_ID`

## Prerequisite

Clone the project

```bash
  git clone https://github.com/kevit-jenish-patel/generative_ai_learning_path_tasks.git
```

Go to the project directory

```bash
  cd OpenAIAssistantsTask
```

Install dependencies from requirements.txt

```bash
  pip install -r requirements.txt
```

Before running the application, set the `OPENAI_ASSISTANT_ID` env variable by running:

```bash
  python src/setup_assistant.py
```

Then copy the assistant id from the terminal output and paste it in your env file
## Run application

Start the application

```bash
  streamlit run src/streamlit_app.py
```

## Authors

- [@jenish](https://www.github.com/kevit-jenish-patel)
