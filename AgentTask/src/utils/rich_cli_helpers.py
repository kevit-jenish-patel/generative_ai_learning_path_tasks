import os

from rich.console import Console as RichConsole
from rich.syntax import Syntax
from rich.panel import Panel

rich_console = RichConsole()

def get_rich_console():
    return rich_console

def display_files(files):
    """Show generated code files using Rich panels."""
    for filename, code in files:
        syntax = Syntax(code, "python", theme="monokai", line_numbers=True)
        panel = Panel(syntax, title=f"[bold green]{filename}[/bold green]", border_style="bright_blue")
        rich_console.print(panel)


def save_files(files):
    """Save generated files into correct directories."""
    for filename, code in files:
        os.makedirs(os.path.dirname(filename) or ".", exist_ok=True)
        with open(filename, "w", encoding="utf-8") as f:
            f.write(code)
    rich_console.print(f"[bold cyan]✅ Saved {len(files)} file(s) successfully.[/bold cyan]")

