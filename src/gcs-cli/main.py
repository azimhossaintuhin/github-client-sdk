import typer
from .auth import authenticate, get_user_info

app = typer.Typer()

# Register commands from auth.py
app.command()(authenticate)
app.command()(get_user_info)

@app.command()
def shell():
    """
    Interactive shell for GitHub CLI.
    """
    typer.echo("🔧 Entering interactive shell mode. Type 'help' or 'exit'.")

    while True:
        command = typer.prompt("gh").strip().lower()

        if command == "exit":
            typer.echo("👋 Exiting shell.")
            break

        elif command == "help":
            typer.echo("Available commands:")
            typer.echo("- authenticate     : Authenticate with GitHub")
            typer.echo("- get-user-info    : Fetch and display user info")
            typer.echo("- exit             : Exit the shell")

        elif command == "authenticate":
            authenticate()

        elif command == "get_user_info":
            get_user_info()

        else:
            typer.secho(f"Unknown command: {command}", fg=typer.colors.RED)


if __name__ == "__main__":
    app()
