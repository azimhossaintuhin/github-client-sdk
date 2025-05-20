from .exceptions import CredentialsError
import httpx
from urllib.parse import urlencode
from .client import GitHubClient


class AuthClient:
    """
    A client for handling GitHub OAuth authentication.

    This class provides methods for generating OAuth authorization URLs and obtaining
    access tokens for GitHub API authentication.

    Parameters
    ----------
    client_id : str
        The GitHub OAuth application client ID
    client_secret : str
        The GitHub OAuth application client secret
    redirect_uri : str, optional
        The callback URL where GitHub will redirect after authorization

    Methods
    -------
    get_auth_url()
        Generates the GitHub OAuth authorization URL for user authentication
    get_access_token(code: str)
        Exchanges an authorization code for an access token

    Raises
    ------
    APIError
        If there's an error in the API response
    """

    def __init__(
        self,
        client_id: str,
        client_secret: str,
        redirect_uri: str = None,
        scope: list[str] = ["user:email"],
    ):
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        self.scope = scope
        if not self.client_id or not self.client_secret:
            raise CredentialsError("client_id and client_secret are required")

    def get_auth_url(self):
        """Generates the OAuth URL for the user to authenticate with GitHub"""
        endpoint = "https://github.com/login/oauth/authorize"
        params = {
            "client_id": self.client_id,
            "redirect_uri": self.redirect_uri,
            "scope": ",".join(self.scope),
            "state": "random_state_string",
            "allow_signup": "true",
        }
        return f"{endpoint}?{urlencode(params)}"

    def get_access_token(self, code: str):
        """Exchanges the code received in the callback for an access token"""
        endpoint = "https://github.com/login/oauth/access_token"
        params = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "code": code,
        }
        headers = {"Accept": "application/json"}
        response = httpx.post(endpoint, params=params, headers=headers)
        response.raise_for_status()
        return response.json().get("access_token")

    def get_user_info(self, token: str):
        """Get user information using the access token"""
        client = GitHubClient(token)
        endpoint = "user"
        response = client.get(endpoint)
        return response
