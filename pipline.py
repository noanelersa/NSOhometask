from api_nasa_client import APInasaClient
from data_transformer import DataTransformer
from astroidService import AsteroidService

class Pipline():
    def __init__ (self,apiKey, db_name):
        self.apiNasaCLient= APInasaClient(apiKey)
        self.data_transform= DataTransformer()
        self.asteroidService = AsteroidService(db_name)

    def run(self, strat_date, end_date):
        print("running all together")