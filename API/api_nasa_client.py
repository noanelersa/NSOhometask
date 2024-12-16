from API.api_client import APIClient
import json
from config import URL



class APInasaClient(APIClient):
    def __init__(self,api_key:str):
        self.api_key=api_key

    def fetch_data(self, start_date:str, end_date:str):
        url= f"{URL}?start_date={start_date}&end_date={end_date}&api_key={self.api_key}"
        data = super().get(url)
        return data


