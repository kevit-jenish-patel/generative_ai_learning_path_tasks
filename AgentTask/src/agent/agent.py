import re,time

from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain.messages import HumanMessage,AIMessage,SystemMessage,ToolMessage

from src.agent.tools import read_file, write_file, clean_code, test_code
from src.core.config import settings

def create_langchain_agent():
    llm = ChatOpenAI(
        model="gpt-5-nano",
        temperature=0,
        api_key=settings.OPENAI_API_KEY
    )

    llm.bind_tools([
        {
            "type": "web_search_preview"
        },
        {
            "type": "code_interpreter",
            "container": {"type": "auto"},
        }
    ])

    system_prompt = (
        "You are a Python coding assistant. "
        "You generate correct, runnable Python code across one or more files as appropriate. "
        "After generating code, you must always use the provided tools to verify correctness. "

        "Your process:\n"
        "1. Generate complete Python code that fulfills the user's request.\n"
        "2. Use the `test_code` tool to run and validate the generated code.\n"
        "3. If the test fails then understand the error and refine the code.\n"
        "4. Format your final response strictly as:\n\n"
        "   # File: path/to/file.py\n"
        "   < code >\n"
        "   # File: another/file.py\n"
        "   < code >\n\n"
        "Rules:\n"
        "- Do not include test or debugging code in the final output.\n"
        "- Never print test results in the final code.\n"
        "- Only return valid, complete Python source files.\n"
    )

    agent = create_agent(
        model=llm,
        tools=[clean_code,test_code],
        system_prompt=system_prompt
    )

    return agent

def generate_agent_response(agent,user_query):
    result = agent.invoke({"messages": [HumanMessage(content=user_query)]})
    return result

def parse_agent_response(response_text: str):
    """
    Parse model output formatted as:
    # File: path/to/file.py
    <code>
    # File: another/file.py
    <code>
    """
    pattern = r"# File: (.*?)\n(.*?)(?=(?:\n# File: )|\Z)"
    matches = re.findall(pattern, response_text, re.DOTALL)

    files = []
    for filename, code in matches:
        files.append((filename.strip(), code.strip()))

    # Fallback: if no matches, treat as a single file
    if not files:
        files.append(("__main__.py", response_text.strip()))

    return files
