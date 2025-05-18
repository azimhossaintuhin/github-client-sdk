from .client import GitHubClient
import base64


class Workflow:
    def __init__(self, client: GitHubClient, username: str, repo: str):
        self.client = client
        self.username = username
        self.repo = repo

    def get_workflows(self, username: str, repo: str):
        endpoint = f"repos/{username}/{repo}/actions/workflows"
        return self.client.get(endpoint)

    def create_workflow(self, workflow_name: str, workflow_path: str):
        endpoint = f"repos/{self.username}/{self.repo}/contents/.github/workflows/{workflow_name}.yaml"
        with open(workflow_path, "rb") as f:
            workflow_content = f.read()

        body = {
            "message": "Create workflow",
            "content": base64.b64encode(workflow_content).decode("utf-8"),
            "branch": "main",
        }
        return self.client.put(endpoint, body)

    def delete_workflow(self, workflow_name: str):
        get_file_url = f"repos/{self.username}/{self.repo}/contents/.github/workflows/{workflow_name}.yaml"
        file_info = self.client.get(get_file_url)
        
        if file_info and "sha" in file_info:
            file_sha = file_info["sha"]
            
            body = {
                "message": f"Delete {workflow_name} workflow",
                "sha": file_sha,
                "branch": "main"
            }
            
            endpoint = f"repos/{self.username}/{self.repo}/contents/.github/workflows/{workflow_name}.yaml"
            return self.client.delete(endpoint, body)
        else:
            return {"error": "Workflow not found or failed to retrieve file SHA"}