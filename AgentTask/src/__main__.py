from src.agent.agent import create_langchain_agent, parse_agent_response, generate_agent_response
from src.utils.rich_cli_helpers import display_files, save_files, rich_console

agent = create_langchain_agent()


def main():
    # result = agent.invoke(
    #     {"messages": [{"role": "user", "content": user_input}]}
    # )

    rich_console.rule("[bold yellow]AI Code Generator[/bold yellow]")
    user_task = rich_console.input("[bold blue]Enter your coding task:[/bold blue] ")

    rich_console.print("\n[bold green]Generating code... please wait[/bold green]\n")

    # Generate code
    result = generate_agent_response(agent, user_task)
    response_text = result["messages"][-1].content

    # Extract files and code
    files = parse_agent_response(response_text)

    rich_console.rule("[bold magenta]Generated Files[/bold magenta]")
    display_files(files)
    save_files(files)

    rich_console.rule("[bold green]Done![/bold green]")

    with open("agent_response.py","w") as f:
        f.write(response_text)

if __name__ == "__main__":
    main()
