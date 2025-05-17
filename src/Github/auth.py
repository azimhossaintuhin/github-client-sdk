from .client import GitHubClient
from .exceptions import APIError

class Auth:
    def __init__(self, client: GitHubClient):
        self.client = client
    
  
    def authentication(self):
        endpoint = "https://github.com/login/oauth/authorize"
        params = {
            "client_id": self.client.client_id,
            "redirect_uri": self.client.redirect_uri,
        }
        return self.client.get(endpoint, params=params)
    
    def callback(self, code: str):
        endpoint = "https://github.com/login/oauth/access_token"
        params = {
            "client_id": self.client.client_id,
            "client_secret": self.client.client_secret,
            "code": code,
        }
        return self.client.post(endpoint, params=params)
    
    
    