"""
GitHub SDK - A Python client for the GitHub API
"""

from .client import GitHubClient
from .exceptions import (
    GitHubError,
    AuthenticationError,
    RateLimitError,
    RepositoryNotFoundError,
    APIError
)

__version__ = "0.1.0"
__all__ = [
    "GitHubClient",
    "GitHubError",
    "AuthenticationError",
    "RateLimitError",
    "RepositoryNotFoundError",
    "APIError"
]
