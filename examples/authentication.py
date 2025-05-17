from Github.auth import AuthClient
import os


def main():
    auth = AuthClient(
        client_id="Ov23liknh8Qr7U5Epfjl",
        client_secret="5d5aec8ed669d1c5d1e00dc4fde1333a580ed954",
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
