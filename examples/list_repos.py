import os
from Github.client import GitHubClient
from Github.repo import Repo
from Github.auth import Auth

def list_repos():
    # Get token from environment variable
    token=os.getenv("TOKEN")
    if not token:
        raise ValueError("Please set the GITHUB_TOKEN environment variable")
        
    client = GitHubClient(token)
    auth = Auth(client)
    username = auth.get_username()
    repo = Repo(client, username)
    repos: list[dict] = repo.get_repos()
    return repos

if __name__ == "__main__":
    repos = list_repos()
    print(repos)