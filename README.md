
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
- ⚙️ **Environment Variable Handling**: Create and update environment variables for GitHub workflows.
- 🧩 **Lightweight & Extensible**: Minimal dependencies and easy to extend for custom needs.
- 🚀 **Supports Python 3.9+**: Compatible with modern Python environments.

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

### Authenticate with GitHub using OAuth

```python
from Github.auth import AuthClient

authClient = AuthClient(
    client_id="your_client_id",
    client_secret="your_client_secret",
    redirect_uri="your_redirect_uri",
    scope=["user:email", "repo", "workflow"]
)

auth_url = authClient.get_auth_url()
print(f"Visit this URL to authorize: {auth_url}")
code = input("Enter the authorization code: ")
token = authClient.get_access_token(code)
user_info = authClient.get_user_info(token)
print(user_info)
```

### Manage GitHub Workflows

```python
import httpx
from Github.client import GitHubClient
from Github.workflow import Workflow

client = GitHubClient(token="your_oauth_token", client=httpx)
workflow = Workflow(client, "github_username", "repository_name")

# List workflows
workflows = workflow.get_workflows("github_username", "repository_name")
print(workflows)

# Create workflow
response = workflow.create_workflow("workflow_name", "path/to/workflow.yml")
print(response)

# Delete workflow
workflow.delete_workflow("workflow_id")
print("Workflow deleted successfully.")
```

### Manage Environment Variables

```python
from Github.variables import VariableClient

variable_client = VariableClient(client, "github_username", "repository_name")

# Create variable
response = variable_client.create_variable("MY_ENV_VAR", "value")
print(response)

# Update variable
response = variable_client.update_variable("MY_ENV_VAR", "new_value")
print(response)
```

## Documentation

Detailed documentation and examples are available at the [GitHub Client SDK Wiki](https://github.com/azimhossaintuhin/github-client-sdk/wiki).

## Contributing

Contributions are welcome! Please read the [CONTRIBUTING.md](CONTRIBUTING.md) guide before submitting a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Related Links

- [GitHub REST API Documentation](https://docs.github.com/en/rest)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [httpx HTTP Client for Python](https://www.python-httpx.org/)

---

