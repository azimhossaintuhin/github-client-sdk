class GitHubError(Exception):
    """Base exception class for all GitHub-related errors."""
    pass

class AuthenticationError(GitHubError):
    """Raised when there are authentication issues with GitHub."""
    pass

class RateLimitError(GitHubError):
    """Raised when GitHub API rate limit is exceeded."""
    pass

class RepositoryNotFoundError(GitHubError):
    """Raised when a requested repository is not found."""
    pass

class APIError(GitHubError):
    """Raised when there's an error in the GitHub API response."""
    def __init__(self, message, status_code=None, response=None):
        self.status_code = status_code
        self.response = response
        super().__init__(message) 
        
class CredentialsError(GitHubError):
    """Raised when there's an error in the GitHub credentials."""
    pass

