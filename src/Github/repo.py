from .client import GitHubClient

class Repo:
    def __init__(self, client: GitHubClient,username:str):
        self.client = client
        self.username = username
        
    
    def get_repos(self):
        endpoint = f"users/{self.username}/repos"
        return self.client.get(endpoint)
    
    def get_repo(self,repo:str):
        endpoint = f"repos/{self.username}/{repo}"
        return self.client.get(endpoint)
    
    def create_repo(self,name:str,description:str=None,private:bool=False):
        endpoint = "user/repos"
        data = {
            "name": name,
            "description": description,
            "private": private,
        }
        return self.client.post(endpoint,data)
    
    def upate_repo(self,repo:str,data:dict):
        endpoint = f"repos/{self.username}/{repo}"
        return self.client.put(endpoint,data)
    
    def delete_repo(self,repo:str):
        endpoint = f"repos/{self.username}/{repo}"
        return self.client.delete(endpoint)     
    

    

        