from clients import GithubClient

class Comments:
    def __init__(self, client: GithubClient,username:str,repo:str):
        self.client = client
        self.username = username
        self.repo = repo
    
        
    def get_comments(self,issue_number:int):
        endpoint = f"repos/{self.username}/{self.repo}/issues/{issue_number}/comments"
        return self.client.get(endpoint)
    
    def create_comment(self,issue_number:int,body:str):
        endpoint = f"repos/{self.username}/{self.repo}/issues/{issue_number}/comments"
        data = {
            "body": body,
        }
        return self.client.post(endpoint,data)

    def update_comment(self,comment_id:int,body:str):
        endpoint = f"repos/{self.username}/{self.repo}/issues/comments/{comment_id}"
        data = {
            "body": body,
        }
        return self.client.put(endpoint,data)

    def delete_comment(self,comment_id:int):
        endpoint = f"repos/{self.username}/{self.repo}/issues/comments/{comment_id}"
        return self.client.delete(endpoint)