import pytest
from unittest.mock import Mock
from src.Github.auth import AuthClient
from src.Github.exceptions import APIError, CredentialsError


# Mock GitHubClient (you need to adjust according to your implementation)
class MockGitHubClient:
    def __init__(self, token):
        self.token = token

    def get(self, endpoint):
        # Simulate a GitHub user info API response
        if endpoint == "user":
            return {
                "login": "testuser",
                "id": 123456,
                "email": "testuser@example.com",
            }
        return {}


# Test suite for AuthClient
class TestAuthClient:
    @pytest.fixture
    def auth_client(self):
        # Create instance of AuthClient with mock credentials
        return AuthClient(
            client_id="test_client_id",
            client_secret="test_client_secret",
            redirect_uri="http://localhost/callback",
        )

    def test_get_auth_url(self, auth_client):
        # Test the URL generation
        auth_url = auth_client.get_auth_url()
        assert "client_id=test_client_id" in auth_url
        assert "scope=user%3Aemail" in auth_url
        assert "state=random_state_string" in auth_url
        assert "allow_signup=true" in auth_url

    @pytest.mark.asyncio
    async def test_get_access_token(self, mocker, auth_client):
        # Mock the POST request for token exchange
        mock_response = Mock()
        mock_response.raise_for_status = Mock()
        mock_response.json.return_value = {"access_token": "mock_access_token"}

        mocker.patch("httpx.post", return_value=mock_response)

        # Exchange code for access token
        token = await auth_client.get_access_token(code="mock_code")
        assert token == "mock_access_token"

    @pytest.mark.asyncio
    async def test_get_user_info(self, mocker, auth_client):
        # Mock the response of getting user info
        mock_response = Mock()
        mock_response.raise_for_status = Mock()
        mock_response.json.return_value = {
            "login": "testuser",
            "id": 123456,
            "email": "testuser@example.com",
        }

        # Mock GitHubClient
        mocker.patch("auth_client.GitHubClient", MockGitHubClient)

        # Get user info using the mock access token
        user_info = await auth_client.get_user_info(token="mock_access_token")
        assert user_info["login"] == "testuser"
        assert user_info["id"] == 123456
        assert user_info["email"] == "testuser@example.com"
