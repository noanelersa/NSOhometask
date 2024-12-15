import requests
from api_client import APIClient


class APInasaClient(APIClient):
    def __init__(self,api_key):
        self.api_key=api_key

    def fetch_data(self, start_date, end_date):
        url= f"https://api.nasa.gov/neo/rest/v1/feed?start_date={start_date}&end_date={end_date}&api_key={self.api_key}"
        result = super().get(url)
        #print (result)
        return result

if __name__ == "__main__":
    api_key = "atGTDOlBIj4CkCcWdEpTTJfQ3okIe5kBnkgRpB0N" 
    nasa_client = APInasaClient(api_key)
    
    data = nasa_client.fetch_data("2024-12-15", "2024-12-22")
    print(data)
