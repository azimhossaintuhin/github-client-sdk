from github_client_sdk.client import GitHubClient
from github_client_sdk.workflow import Workflow
from github_client_sdk.auth import AuthClient
import os


def main():
    authClient = AuthClient(
        client_id=os.getenv("CLIENT_ID"),
        client_secret=os.getenv("CLIENT_SECRET"),
        redirect_uri="http://localhost:8000/callback",
        scope=["repo", "user:email", "workflow"],
    )
    auth_url = authClient.get_auth_url()
    print(auth_url)
    code = input("Enter the Code: ")
    token = authClient.get_access_token(code)

    get_user = authClient.get_user_info(token)

    if not get_user:
        print("Failed to get user info")
        return

    client = GitHubClient(token=token)

    username = get_user["login"]
    repo = "blog"

    workflow = Workflow(client, username, repo)

    workflows = workflow.get_workflows(username, repo).get("workflows")
    if workflows:
        workflow_name = workflows[0].get("path").split("/")[-1].split(".")[0]
        workflow.delete_workflow(workflow_name)
        print(f"Deleted workflow with ID: {workflow_name}")
    else:
        print("No workflows found in the repository.")


if __name__ == "__main__":
    main()
