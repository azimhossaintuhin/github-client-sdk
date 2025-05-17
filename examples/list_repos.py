import os
from Github.client import GitHubClient
from Github.repo import Repo


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
