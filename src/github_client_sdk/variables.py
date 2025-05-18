from .client import GitHubClient


class Variables:
    def __init__(self, client: GitHubClient, username: str, repo: str):
        self.client = client
        self.username = username
        self.repo = repo

    def get_variables(self):
        endpoint = f"repos/{self.username}/{self.repo}/actions/variables"
        return self.client.get(endpoint)

    def get_variable(self, variable_name: str):
        endpoint = (
            f"repos/{self.username}/{self.repo}/actions/variables/{variable_name}"
        )
        return self.client.get(endpoint)

    def create_variable(self, variable_name: str, value: str):
        endpoint = f"repos/{self.username}/{self.repo}/actions/variables"
        return self.client.post(endpoint, {"name": variable_name, "value": value})

    def update_variable(self, variable_name: str, value: str):
        endpoint = (
            f"repos/{self.username}/{self.repo}/actions/variables/{variable_name}"
        )
        return self.client.put(endpoint, {"name": variable_name, "value": value})

    def delete_variable(self, variable_name: str):
        endpoint = (
            f"repos/{self.username}/{self.repo}/actions/variables/{variable_name}"
        )
        return self.client.delete(endpoint)
