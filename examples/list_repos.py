import os
from github_client_sdk.client import GitHubClient
from github_client_sdk.repo import Repo


def list_repos():
    token = os.getenv("Token")
    
    if not token:
        raise ValueError("Please set the GITHUB_TOKEN environment variable")

    client = GitHubClient(token)

    username = "azimhossaintuhin"
    repo = Repo(client, username)
    repos: list[dict] = repo.get_repos()
    return repos


if __name__ == "__main__":
    repos = list_repos()
    print(repos)
