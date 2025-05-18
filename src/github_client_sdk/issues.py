from github_client_sdk.client import GitHubClient

class Issues:
    def __init__(self, client: GitHubClient,username:str,repo:str):
        self.client = client
        self.username = username
        self.repo = repo
        
    def get_issues(self):
        endpoint = f"repos/{self.username}/{self.repo}/issues"
        return self.client.get(endpoint)
        
    def get_issue(self,issue_number:int):
        endpoint = f"repos/{self.username}/{self.repo}/issues/{issue_number}"
        return self.client.get(endpoint)
    
    def create_issue(self,title:str,body:str=None,labels:list=None):
        endpoint = f"repos/{self.username}/{self.repo}/issues"
        data = {
            "title": title,
            "body": body,
            "labels": labels,
        }
        return self.client.post(endpoint,data)
    
    def update_issue(self,issue_number:int,title:str=None,body:str=None,labels:list=None):
        endpoint = f"repos/{self.username}/{self.repo}/issues/{issue_number}"
        data = {
            "title": title,
            "body": body,
            "labels": labels,
        }
        return self.client.put(endpoint,data)
        
        
    def delete_issue(self,issue_number:int):
        endpoint = f"repos/{self.username}/{self.repo}/issues/{issue_number}"
        return self.client.delete(endpoint)
    
 
    
    
    