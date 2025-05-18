from Github.auth import AuthClient
from Github.client import GitHubClient
from Github.variables import Variables
import os


def get_variables(client, get_user):
    variables = Variables(client, get_user["login"], "blog")

    print(variables.get_variables())


def create_variable(client, get_user):
    variables = Variables(client, get_user["login"], "blog")
    variables.create_variable("TEST_VARIABLE", "TEST_VALUE")
    print(variables.get_variable("TEST_VARIABLE"))


def update_variable(client, get_user):
    variables = Variables(client, get_user["login"], "blog")
    variables.update_variable("TEST_VARIABLE", "TEST_VALUE_UPDATED")
    print(variables.get_variable("TEST_VARIABLE"))


def delete_variable(client, get_user):
    variables = Variables(client, get_user["login"], "blog")
    variables.delete_variable("TEST_VARIABLE")
    print(variables.get_variable("TEST_VARIABLE"))


def main():
    auth = AuthClient(
        client_id=os.getenv("CLIENT_ID"),
        client_secret=os.getenv("CLIENT_SECRET"),
        redirect_uri="http://localhost:8000/callback",
        scope=["repo", "user:email", "workflow"],
    )
    print(auth.get_auth_url())
    code = input("Enter the Code: ")
    token = auth.get_access_token(code)
    get_user = auth.get_user_info(token)

    client = GitHubClient(token=token)

    print("Getting variables")
    get_variables(client, get_user)

    print("Creating variable")
    create_variable(client, get_user)

    print("Updating variable")
    update_variable(client, get_user)

    print("Deleting variable")
    delete_variable(client, get_user)


if __name__ == "__main__":
    main()
