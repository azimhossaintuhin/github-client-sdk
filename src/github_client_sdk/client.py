import httpx
from .exceptions import GitHubError, APIError, AuthenticationError



class GitHubClient:
    """
    A client for interacting with the GitHub API.

    This class provides a high-level interface to interact with the GitHub REST API.
    It handles authentication, rate limiting, and common API operations.

    Parameters
    ----------
    token : str
        GitHub Personal Access Token for authentication.
        Required for accessing private repositories and making authenticated requests.

    Attributes
    ----------
    base_url : str
        The base URL for GitHub API requests (default: 'https://api.github.com')
    headers : dict
        HTTP headers including authentication token and content type

    Methods
    -------
    get(endpoint: str, params: dict = None) -> dict
        Make a GET request to the GitHub API.
        Returns the JSON response as a dictionary.

    post(endpoint: str, data: dict = None) -> dict
        Make a POST request to the GitHub API.
        Returns the JSON response as a dictionary.

    put(endpoint: str, data: dict = None) -> dict
        Make a PUT request to the GitHub API.
        Returns the JSON response as a dictionary.

    delete(endpoint: str) -> bool
        Make a DELETE request to the GitHub API.
        Returns True if successful.

    Raises
    ------
    AuthenticationError
        If the provided token is invalid or expired.
    RateLimitError
        If the GitHub API rate limit is exceeded.
    APIError
        If there's an error in the API response.
    """

    # befor creating the class


    def __init__(self, token: str):
        self.token = token
        self.base_url = "https://api.github.com"
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/vnd.github.v3+json",
        }
        self.client = httpx.Client(
            base_url=self.base_url,
            headers=self.headers,
            timeout=30,
        )


    # Get request
    def get(self, endpoint: str, params: dict = None):
        try:
            url = f"{self.base_url}/{endpoint}"
            response = self.client.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            raise APIError(f"HTTP error occurred: {e}")
        except Exception as e:
            raise GitHubError(f"An error occurred: {e}")

    # post request
    def post(self, endpoint: str, data: dict = None, params: dict = None):
        try:
            url = f"{self.base_url}/{endpoint}"
            response = self.client.post(url, json=data, params=params)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            raise Exception(f"HTTP error occurred: {e}")
        except Exception as e:
            raise Exception(f"An error occurred: {e}")

    # put request
    def put(self, endpoint: str, data: dict = None, params: dict = None):
        try:
            url = f"{self.base_url}/{endpoint}"
            response = self.client.put(url, json=data, params=params)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            raise Exception(f"HTTP error occurred: {e}")
        except Exception as e:
            raise Exception(f"An error occurred: {e}")

    # delete request
    def delete(self, endpoint: str, params: dict = None):
        try:
            url = f"{self.base_url}/{endpoint}"
            response = self.client.delete(url, params=params)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            raise Exception(f"HTTP error occurred: {e}")
        except Exception as e:
            raise Exception(f"An error occurred: {e}")
