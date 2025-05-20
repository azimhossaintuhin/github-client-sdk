import typer
from github_client_sdk.auth import AuthClient 
import os
import pathlib
from tabulate import tabulate


app = typer.Typer(name="gcs-cli")


def get_env_file_location():
    return pathlib.Path(__file__).parent.parent.parent / ".env"


def load_env():
    with open(get_env_file_location(), "r") as f:
        for line in f:
            key, value = line.strip().split("=")
            os.environ[key] = value
env = load_env()




def get_access_token():
    with open(get_env_file_location(), "r") as f:
        for line in f:
            key, value = line.strip().split("=")
            if key == "GITHUB_ACCESS_TOKEN":
                return value
    return None

@app.command()
def authenticate():

    # Check if already authenticated
    if get_access_token():
        typer.secho("✅ Already authenticated", fg=typer.colors.GREEN)
        return

    # Get client ID, secret, callback URL, and scopes
    client_id = typer.prompt("Enter the client ID")
    client_secret = typer.prompt("Enter the client secret")
    callback_url = typer.prompt("Enter the callback URL")
    scopes = typer.prompt("Enter the scopes (comma separated)").split(",")
    
    # Authenticate
    try:
        auth_client = AuthClient(
            client_id=client_id,
            client_secret=client_secret,
            redirect_uri=callback_url,
            scope=scopes,
        )
        auth_url = auth_client.get_auth_url()
        typer.echo(f"Please visit the following URL to authenticate: {auth_url}")
        code = typer.prompt("Enter the code from the callback URL")
        access_token = auth_client.get_access_token(code=code)

        # Store credentials
        with open(get_env_file_location(), "w") as f:
            f.write(f"GITHUB_CLIENT_ID={client_id}\n")
            f.write(f"GITHUB_CLIENT_SECRET={client_secret}\n")
            f.write(f"GITHUB_CALLBACK_URL={callback_url}\n")
            f.write(f"GITHUB_SCOPES={','.join(scopes)}\n")
            f.write(f"GITHUB_ACCESS_TOKEN={access_token}\n")
        typer.secho("✅ Authentication successful", fg=typer.colors.GREEN)
    except Exception as e:
        typer.secho(f"Error: {e}", fg=typer.colors.RED)
        raise typer.Abort()

@app.command(
    help="Get user info",
    short_help="Get user info",
    epilog="Get user info",
    add_help_option=True,
)
def get_user_info():
    load_env()
    access_token = get_access_token()
    if not access_token:
        typer.secho("No access token found", fg=typer.colors.RED)
        raise typer.Abort()
    auth_client = AuthClient(
        client_id=os.environ["GITHUB_CLIENT_ID"],
        client_secret=os.environ["GITHUB_CLIENT_SECRET"],
        redirect_uri=os.environ["GITHUB_CALLBACK_URL"],
        scope=os.environ["GITHUB_SCOPES"].split(","),
    )
    user = auth_client.get_user_info(token=access_token)
    user_info = {
        "login": user["login"],
        "name": user["name"],
        "email": user["email"],
        "location": user["location"],
        "company": user["company"],
        "followers": user["followers"],
        "public_repos": user["public_repos"],
       
    }
    user_table = tabulate([user_info], headers="keys", tablefmt="grid")
    typer.echo(user_table)


