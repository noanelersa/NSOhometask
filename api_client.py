import requests

class APIClient:
    def get(self,url):
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except Exception as err:
            print('Creation failed: \nError: %s' % str(err))

    
