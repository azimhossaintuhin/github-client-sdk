from Github.auth import AuthClient
import os


def main():
    auth = AuthClient(
        client_id=os.getenv("CLIENT_ID"),
        client_secret=os.getenv("CLIENT_SECRET"),
        redirect_uri="http://localhost:8000/callback",
        scope=["repo", "user:email", "workflow"],
    )
    print(auth.get_auth_url())

    code = input("Enter the code: ")
    access_token = auth.get_access_token(code)
    print(access_token)

    user_info = auth.get_user_info(access_token)
    print(user_info)


if __name__ == "__main__":
    main()
