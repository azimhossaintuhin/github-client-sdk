from github_client_sdk.client import GitHubClient
from github_client_sdk.auth import AuthClient
from  github_client_sdk.variables import Variables
from ..helpers.load_env import load_env ,get_env_file_location
from  github_client_sdk.repo import Repo
from tabulate import tabulate
import typer
from rich import print
import os
app = typer.Typer()
load_env()
client = GitHubClient(token=os.getenv("GITHUB_ACCESS_TOKEN"))

@app.command()
def get_env_variables():
    get_all_repos = Repo(client,os.getenv("GITHUB_USERNAME"))
    all_repos = []
    all_variables = []
    for repo in get_all_repos.get_repos():
        data = {
            "id":repo.get("id"),
            "name":repo.get("name"),
            "private":repo.get("private"),
        }
        all_repos.append(data)
    typer.echo(tabulate(all_repos, headers="keys",tablefmt="grid"))
    repo_name = typer.prompt("Enter the repo name")
    variables = Variables(client,os.getenv("GITHUB_USERNAME"),repo_name)
    if  variables.get_variables().get("total_count") == 0:
        typer.echo("No variables found")
        return
    for variable in variables.get_variables().get("variables"):
        data = {
            "key":variable.get("name"),
            "value":variable.get("value"),
        }
        all_variables.append(data)
    typer.echo(tabulate(all_variables, headers="keys",tablefmt="grid"))


@app.command()
def set_env_variable():
    get_all_repos = Repo(client,os.getenv("GITHUB_USERNAME"))
    all_repos = []
    all_variables = []
    for repo in get_all_repos.get_repos():
        data = {
            "id":repo.get("id"),
            "name":repo.get("name"),
            "private":repo.get("private"),
        }
        all_repos.append(data)
    typer.echo(tabulate(all_repos, headers="keys",tablefmt="grid"))
    repo_name = typer.prompt("Enter the repo name")
    variables = Variables(client,os.getenv("GITHUB_USERNAME"),repo_name)
    set_Variable_count = typer.prompt("Enter the number of variables to set")
    for i in range(int(set_Variable_count)):
        variable_name = typer.prompt("Enter the variable name")
        variable_value = typer.prompt("Enter the variable value")
        variables.create_variable(variable_name,variable_value)
    typer.echo("Variables set successfully")
    for variable in variables.get_variables().get("variables"):
        data = {
            "key":variable.get("name"),
            "value":variable.get("value"),
        }
        all_variables.append(data)
    typer.echo(tabulate(all_variables, headers="keys",tablefmt="grid"))
    