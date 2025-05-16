import httpx


class GithubClient:
    def __init__(self, token: str):
        self.token = token
        self.base_url = "https://api.github.com"
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/vnd.github.v3+json",
        }
        self.client = httpx.Client(
            base_url=self.base_url,
            headers=self.headers,
            timeout=30,
        )
        
    # Get request
    def get(self, endpoint:str,params:dict=None):
        try:
            url = f"{self.base_url}/{endpoint}"
            response = self.client.get(url,params=params)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            raise Exception(f"HTTP error occurred: {e}")
        except Exception as e:
            raise Exception(f"An error occurred: {e}")
        
    # post request
    def post(self, endpoint:str,data:dict=None , params:dict=None):
        try:
            url = f"{self.base_url}/{endpoint}"
            response = self.client.post(url,json=data,params=params)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            raise Exception(f"HTTP error occurred: {e}")
        except Exception as e:
            raise Exception(f"An error occurred: {e}")

    # put request
    def put(self, endpoint:str,data:dict=None , params:dict=None):
        try:
            url = f"{self.base_url}/{endpoint}"
            response = self.client.put(url,json=data,params=params)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            raise Exception(f"HTTP error occurred: {e}")
        except Exception as e:
            raise Exception(f"An error occurred: {e}")
    
    # delete request
    def delete(self, endpoint:str,params:dict=None):
        try:
            url = f"{self.base_url}/{endpoint}"
            response = self.client.delete(url,params=params)
            response.raise_for_status()
            return response.json() 
        except httpx.HTTPStatusError as e:
            raise Exception(f"HTTP error occurred: {e}")
        except Exception as e:
            raise Exception(f"An error occurred: {e}")
        
        
        
        