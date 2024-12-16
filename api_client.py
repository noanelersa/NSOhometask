import requests

class APIClient:
    def get(self,url):
        try:
            response = requests.get(url)
            response.raise_for_status() #check if it worked- 200 ok?
            return response.json()
        except Exception as err:
            print('Creation failed: \nError: %s' % str(err))

    
