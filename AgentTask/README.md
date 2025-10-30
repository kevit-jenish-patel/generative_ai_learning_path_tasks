
# AutoPy

The AI Code Generator is a command-line Python tool that allows users to generate Python code for a specified task using an AI agent.

## Features

- **Interactive CLI**: Users input their coding tasks directly in the terminal.
- **AI-Powered Code Generation**: Uses a GPT-5 based model via LangChain to generate Python code.
- **Multi-file Support**: Handles generating multiple files with proper file paths.
- **Code Testing Tools**: Automatically validates generated code using sandboxed testing functions.
- **Rich CLI Output**: Displays generated files and statuses using the `rich` library.
- **Automatic Saving**: Saves generated code files to disk for immediate use.


## Tech Stack

- **LangChain**: For AI agent orchestration and tool binding.

- **OpenAI GPT-5 Nano**: The language model for code generation.

- **Rich**: For enhanced terminal output and status spinners.


## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`OPENAI_API_KEY`
## Run application

Clone the project

```bash
  git clone https://github.com/kevit-jenish-patel/generative_ai_learning_path_tasks.git
```

Go to the project directory

```bash
  cd AgentTask
```

Install dependencies from requirements.txt

```bash
  pip install -r requirements.txt
```

Start the application

```bash
  python src/__main__.py
```

## Authors

- [@jenish](https://www.github.com/kevit-jenish-patel)

