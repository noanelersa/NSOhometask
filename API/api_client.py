import requests
from abc import ABC


class APIClient(ABC):
    def get(self, url: str):
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except Exception as err:
            print('Creation failed: \nError: %s' % str(err))
