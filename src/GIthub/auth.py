from clients import GithubClient

class Auth:
    def __init__(self, client: GithubClient):
        self.client = client
        
        
    def get_auth_user(self):
        endpoint = "user"
        return self.client.get(endpoint)
    
    def get_auth_user_emails(self):
        endpoint = "user/emails"
        return self.client.get(endpoint)

    def get_auth_user_keys(self):
        endpoint = "user/keys"
        return self.client.get(endpoint)
    
    def get_auth_user_orgs(self):
        endpoint = "user/orgs"
        return self.client.get(endpoint)