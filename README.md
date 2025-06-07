# GitHub Client SDK — Python Library for GitHub API Automation

[![PyPI version](https://img.shields.io/pypi/v/github-client-sdk.svg)](https://pypi.org/project/github-client-sdk/)
[![Python Version](https://img.shields.io/pypi/pyversions/github-client-sdk.svg)](https://pypi.org/project/github-client-sdk/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Build Status](https://img.shields.io/github/actions/workflow/status/azimhossaintuhin/github-client-sdk/python-package.yml)](https://github.com/azimhossaintuhin/github-client-sdk/actions)
[![Downloads](https://pepy.tech/badge/github-client-sdk)](https://pepy.tech/project/github-client-sdk)

## Overview

**GitHub Client SDK** is a powerful and easy-to-use **Python library** designed to simplify interaction with the **GitHub REST API v3** and automate **GitHub Actions workflows**, **environment variables**, and repository management tasks. 

This SDK provides a clean interface for developers, DevOps engineers, and automation specialists to seamlessly integrate GitHub operations into Python projects and CI/CD pipelines.

## Key Features

- 🔄 **GitHub Actions Workflow Management**: Create, list, and delete workflows effortlessly via Python.
- 🔐 **OAuth Authentication Support**: Securely authenticate using OAuth tokens.
- ⚙️ **Environment Variable Handling**: Create, update, and delete environment variables for GitHub workflows.
- 🧩 **Lightweight & Extensible**: Minimal dependencies and easy to extend for custom needs.
- 🚀 **Supports Python 3.9+**: Compatible with modern Python environments.
- 💻 **Interactive CLI**: Built-in command-line interface for easy interaction.

## Installation

Install the latest version of **GitHub Client SDK** directly from PyPI:

```bash
pip install github-client-sdk
```

Or clone the repository and install dependencies:

```bash
git clone https://github.com/azimhossaintuhin/github-client-sdk.git
cd github-client-sdk
pip install -r requirements.txt
```

## Quick Start Guide

### Authentication

```python
from github_client_sdk.auth import AuthClient
import os

# Initialize the auth client
auth = AuthClient(
    client_id=os.getenv("CLIENT_ID"),
    client_secret=os.getenv("CLIENT_SECRET"),
    redirect_uri="http://localhost:8000/callback",
    scope=["repo", "user:email", "workflow"]
)

# Get authentication URL
auth_url = auth.get_auth_url()
print(f"Visit this URL to authorize: {auth_url}")

# Get access token
code = input("Enter the authorization code: ")
access_token = auth.get_access_token(code)

# Get user information
user_info = auth.get_user_info(access_token)
print(user_info)
```

### Managing Workflows

```python
from github_client_sdk.client import GitHubClient
from github_client_sdk.workflow import Workflow

# Initialize the client
client = GitHubClient(token="your_oauth_token")

# Create workflow instance
workflow = Workflow(client, "username", "repository_name")

# Create a new workflow
workflow_name = "new-workflow"
workflow_path = "path/to/workflow.yaml"
response = workflow.create_workflow(workflow_name, workflow_path)
print(f"Workflow creation response: {response}")

# List workflows
workflows = workflow.get_workflows()
print(workflows)

# Delete workflow
workflow.delete_workflow("workflow_id")
```

### Managing Environment Variables

```python
from github_client_sdk.variables import Variables

# Initialize variables client
variables = Variables(client, "username", "repository_name")

# Get all variables
all_variables = variables.get_variables()
print(all_variables)

# Create a new variable
variables.create_variable("TEST_VARIABLE", "TEST_VALUE")

# Update an existing variable
variables.update_variable("TEST_VARIABLE", "NEW_VALUE")

# Get a specific variable
variable = variables.get_variable("TEST_VARIABLE")
print(variable)

# Delete a variable
variables.delete_variable("TEST_VARIABLE")
```

### Using the CLI

The SDK comes with a built-in CLI for easy interaction:

```bash
# Start the interactive shell
github-client-shell

# Available commands in the shell:
# 1. authenticate     : Authenticate with GitHub
# 2. get-user-info   : Fetch and display user info
# 3. set-env-variable: Set environment variables
# 4. get-env-variables: Get environment variables
# 5. logout          : Logout from GitHub
# 6. clear           : Clear the screen
# 7. exit            : Exit the shell
```

## Environment Variables

The SDK requires the following environment variables to be set:

- `CLIENT_ID`: Your GitHub OAuth App client ID
- `CLIENT_SECRET`: Your GitHub OAuth App client secret

## Contributing

Contributions are welcome! Please read the [CONTRIBUTING.md](CONTRIBUTING.md) guide before submitting a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Related Links

- [GitHub REST API Documentation](https://docs.github.com/en/rest)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [GitHub OAuth Apps Documentation](https://docs.github.com/en/developers/apps/building-oauth-apps)

---

