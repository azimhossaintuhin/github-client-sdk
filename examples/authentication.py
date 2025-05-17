from Github.auth import AuthClient
import os


def main():
    auth = AuthClient(
        client_id="client_id",
        client_secret="client_secret",
        redirect_uri="http://localhost:8000/callback",
    )
    print(auth.get_auth_url())

    code = input("Enter the code: ")
    access_token = auth.get_access_token(code)
    print(access_token)

    user_info = auth.get_user_info(access_token)
    print(user_info)


if __name__ == "__main__":
    main()
