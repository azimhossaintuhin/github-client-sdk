from Github.client import GitHubClient
from Github.workflow import Workflow
from Github.auth import AuthClient
import os


def main():
    authClient = AuthClient(
        client_id=os.getenv("CLIENT_ID"),
        client_secret=os.getenv("CLIENT_SECRET"),
        redirect_uri="http://localhost:8000/callback",
        scope=["repo", "user:email", "workflow",]
    )
    auth_url = authClient.get_auth_url()
    print(auth_url)
    code = input("Enter the Code: ")
    token = authClient.get_access_token(code)
    get_user = authClient.get_user_info(token)

    client = GitHubClient(token=token)

    username = get_user["login"]
    repo = "blog"

    workflow = Workflow(client, username, repo)

    workflow_name = "new-workflow"
    workflow_path = os.path.join(os.path.dirname(__file__), "demo.yaml")

    response = workflow.create_workflow(workflow_name, workflow_path)

    print(f"Workflow creation response: {response}")


if __name__ == "__main__":
    main()
