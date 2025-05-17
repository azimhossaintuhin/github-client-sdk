from .client import GitHubClient
from .exceptions import APIError

class Auth:
    def __init__(self, client: GitHubClient):
        self.client = client
        
        
    def get_auth_user(self):
        try:
            endpoint = "user"
            return self.client.get(endpoint)
        
        except APIError as e:
            print(e)
            
        except Exception as e:
            raise APIError("Failed to get auth user" , e , 401)
    
    def get_username(self):
        try:
            return self.get_auth_user()["login"]
        except APIError as e:
            print(e)
        except Exception as e:
            print(e)
            raise APIError("Failed to get username" , e , 401)
    
    def get_auth_user_emails(self):
        endpoint = "user/emails"
        return self.client.get(endpoint)

    def get_auth_user_keys(self):
        endpoint = "user/keys"
        return self.client.get(endpoint)
    
    def get_auth_user_orgs(self):
        endpoint = "user/orgs"
        return self.client.get(endpoint)