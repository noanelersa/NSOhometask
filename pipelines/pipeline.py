from API.api_nasa_client import APInasaClient
from transformers.data_transformer import DataTransformer
from database.astroidService import AsteroidService
from config import ASTEROID_LIMIT


class Pipeline():
    def __init__(self, apiKey: str, db_name: str):
        self.apiNasaCLient = APInasaClient(apiKey)
        self.data_transform = DataTransformer()
        self.asteroidService = AsteroidService(db_name)

    def run(self, start_date: str, end_date: str) -> None:
        try:

            apiData = self.apiNasaCLient.fetch_data(start_date, end_date)
            print("got the data from the API")

            transformedData = self.data_transform.transform(apiData)
            print("transformed the data")

            for asteroid in transformedData:
                self.asteroidService.insert_asteroids(asteroid)
            print("stored the asteroids into the db")

            print(f"the {ASTEROID_LIMIT} largest asteroids by diameter are:")
            print(self.asteroidService.find_5_largest_asteroids())

        except Exception as err:
            print('Creation failed: \nError: %s' % str(err))
        finally:
            self.asteroidService.closeDBconnection()
