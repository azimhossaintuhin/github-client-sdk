
# GitHub Client

The **GitHub Client** is a robust Python library designed for seamless interaction with the GitHub API. It offers an intuitive interface for managing GitHub workflows, environment variables, and various repository actions. This SDK simplifies automation tasks such as workflow management and environment variable configuration, making it ideal for developers looking to integrate GitHub operations into their Python projects.

## Features

- **Workflow Management**: Effortlessly create, list, and delete GitHub Actions workflows.
- **Environment Variable Management**: Create and update environment variables for GitHub Actions workflows.
- **OAuth Authentication**: Secure OAuth authentication for accessing GitHub repositories and performing operations.
- **Easy Integration**: Lightweight and easy to integrate into your existing Python projects.
- **Extensible**: Designed for further extensions and customization as per your workflow automation needs.

## Installation

To install and set up the **GitHub Client**, clone the repository and install the required dependencies:

```bash
git clone https://github.com/azimhossaintuhin/Github_SDK.git
cd Github_SDK
pip install -r requirements.txt
```

### Requirements

- Python 3.x or higher
- `httpx` library (installed via `requirements.txt`)
- A GitHub account and OAuth token for authentication

## Usage

### Authentication

To use the SDK, you need to authenticate via OAuth using your GitHub credentials. Follow the steps below:

```python
from Github.auth import AuthClient

authClient = AuthClient(
    client_id="your_client_id",
    client_secret="your_client_secret",
    redirect_uri="your_redirect_uri"
)

auth_url = authClient.get_auth_url()
print(f"Please visit this URL to authorize the application: {auth_url}")
code = input("Enter the Code you received after authorization: ")
token = authClient.get_access_token(code)
user_info = authClient.get_user_info(token)
```

### Working with Workflows

You can interact with GitHub Actions workflows in your repository using the `Workflow` class.

#### List Workflows

To retrieve and list all workflows in a repository:

```python
import httpx
from Github.client import GitHubClient
from Github.workflow import Workflow

client = GitHubClient(token="your_oauth_token", client=httpx)
workflow = Workflow(client, "your_github_username", "your_repository_name")

workflows = workflow.get_workflows("your_github_username", "your_repository_name")
print(workflows)
```

#### Create Workflow

To create a new workflow in the specified repository:

```python
workflow_name = "my_new_workflow"
workflow_path = "path/to/your/workflow.yml"

response = workflow.create_workflow(workflow_name, workflow_path)
print(f"Workflow created successfully: {response}")
```

#### Delete Workflow

To delete a specific workflow by its ID:

```python
workflow_id = "your_workflow_id"
workflow.delete_workflow(workflow_id)
print(f"Workflow {workflow_id} deleted successfully.")
```

### Working with Environment Variables

The SDK also allows you to manage environment variables for your workflows.

#### Create Variable

To create a new environment variable:

```python
import httpx
from Github.variables import VariableClient

variable_client = VariableClient(client, "your_github_username", "your_repository_name")

response = variable_client.create_variable("MY_ENV_VAR", "my_value")
print(f"Environment variable created: {response}")
```

#### Update Variable

To update the value of an existing environment variable:

```python
response = variable_client.update_variable("MY_ENV_VAR", "new_value")
print(f"Environment variable updated: {response}")
```

## Contributing

We welcome contributions to the **GitHub Client**. If you'd like to contribute, please follow the steps below:

1. Fork the repository.
2. Create a new branch for your feature or bugfix (`git checkout -b feature-branch`).
3. Commit your changes with a clear and concise message (`git commit -am 'Add new feature'`).
4. Push your changes to your fork (`git push origin feature-branch`).
5. Create a pull request explaining your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [GitHub API Documentation](https://docs.github.com/en/rest)
- [Python httpx Library](https://www.python-httpx.org/)
- [GitHub Actions](https://docs.github.com/en/actions)