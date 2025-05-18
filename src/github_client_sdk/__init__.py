"""
GitHub Client SDK - A Python SDK for interacting with the GitHub API
"""

from .client import GitHubClient
from .exceptions import (
    GitHubError,
    AuthenticationError,
    RateLimitError,
    RepositoryNotFoundError,
    APIError,
)

__version__ = "0.1.0"
__name__ = "github-client-sdk"
__all__ = [
    "GitHubClient",
    "GitHubError",
    "AuthenticationError",
    "RateLimitError",
    "RepositoryNotFoundError",
    "APIError",
]
