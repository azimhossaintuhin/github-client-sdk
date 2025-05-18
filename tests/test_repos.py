import pytest
from src.github_client_sdk.repo import Repo
from github_client_sdk.client import GitHubClient
from unittest.mock import MagicMock


@pytest.fixture
def mock_client():
    client = MagicMock(spec=GitHubClient)

    return client               


@pytest.fixture
def repo(mock_client):
    return Repo(client=mock_client, username="testuser")


def test_get_repos(repo, mock_client):
    mock_client.get.return_value = [{"name": "test-repo"}]

    repos = repo.get_repos()

    mock_client.get.assert_called_once_with("users/testuser/repos")
    assert repos == [{"name": "test-repo"}]


def test_get_repo(repo, mock_client):
    mock_client.get.return_value = {"name": "test-repo"}

    result = repo.get_repo("test-repo")

    mock_client.get.assert_called_once_with("repos/testuser/test-repo")
    assert result["name"] == "test-repo"


def test_create_repo(repo, mock_client):
    mock_client.post.return_value = {"name": "new-repo"}

    result = repo.create_repo(name="new-repo", description="desc", private=True)

    mock_client.post.assert_called_once_with(
        "user/repos",
        {
            "name": "new-repo",
            "description": "desc",
            "private": True,
        },
    )
    assert result["name"] == "new-repo"


def test_update_repo(repo, mock_client):
    mock_client.put.return_value = {"name": "updated-repo"}

    result = repo.upate_repo("repo-name", {"description": "new desc"})

    mock_client.put.assert_called_once_with(
        "repos/testuser/repo-name", {"description": "new desc"}
    )
    assert result["name"] == "updated-repo"


def test_delete_repo(repo, mock_client):
    mock_client.delete.return_value = {"message": "Deleted"}

    result = repo.delete_repo("repo-name")

    mock_client.delete.assert_called_once_with("repos/testuser/repo-name")
    assert result["message"] == "Deleted"
