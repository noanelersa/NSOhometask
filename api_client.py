import requests

class APIClient:
    def get(self,url):
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

    
