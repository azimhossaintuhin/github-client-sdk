import typer
from rich.prompt import Prompt
from gcs_cli.utils.auth import authenticate, get_user_info,logout
from gcs_cli.utils.envVariables import get_env_variables, set_env_variable

app = typer.Typer(help="GitHub Client SDK CLI")

# Register commands from auth.py
app.command()(authenticate)
app.command()(get_user_info)
app.command()(get_env_variables)
app.command()(set_env_variable)
app.command()(logout)
@app.command()
def shell():
    """
    Interactive shell for GitHub CLI.
    """
    typer.echo("🔧 Entering interactive shell mode. Type 'help' or 'exit'.")

    while True:
        command = Prompt.ask("[bold green]github-client-shell[/bold green]").strip().lower()

        if command == "exit":
            typer.echo("👋 Exiting shell.")
            break   

        elif command == "help" or command == "ls":
            typer.echo("\nAvailable commands:")
            typer.echo("1. authenticate     : Authenticate with GitHub")
            typer.echo("2. get-user-info    : Fetch and display user info")
            typer.echo("3. set-env-variable : Set environment variables")
            typer.echo("4. get-env-variables: Get environment variables")
            typer.echo("5. logout          : Logout from GitHub")
            typer.echo("6. clear           : Clear the screen")
            typer.echo("7. exit            : Exit the shell")
        elif command == 'clear':
            typer.clear()
            continue
        elif command == "authenticate" or command == "1":
            authenticate()
        elif command == "get-user-info" or command == "2":
            get_user_info()
        elif command == "set-env-variable" or command == "3":
            set_env_variable()
        elif command == "get-env-variables" or command == "4":
            get_env_variables()
        elif command == "logout" or command == "5":
            logout()
        else:
            typer.secho(f"Unknown command: {command}", fg=typer.colors.RED)

def main():
    import sys
    # If no arguments are provided, start the shell
    if len(sys.argv) == 1:
        shell()
    else:
        app()

if __name__ == "__main__":
    main()
# 5d0c83b372f22a19d420a6565b436e8f48442c15
# Ov23liknh8Qr7U5Epfjl
# http://localhost:8000/