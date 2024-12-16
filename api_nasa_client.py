import requests
from api_client import APIClient
import json


class APInasaClient(APIClient):
    def __init__(self,api_key):
        self.api_key=api_key

    def fetch_data(self, start_date, end_date):
        url= f"https://api.nasa.gov/neo/rest/v1/feed?start_date={start_date}&end_date={end_date}&api_key={self.api_key}"
        data = super().get(url)
        #print (data)
        #opening the json to a file to configure its sturcture for the transformer function
        with open("nasa_data.json", "w") as file:
            json.dump(data, file, indent=4)
        return data


