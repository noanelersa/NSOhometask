from api_nasa_client import APInasaClient
from data_transformer import DataTransformer
from astroidService import AsteroidService

class Pipline():
    def __init__ (self,apiKey, db_name):
        self.apiNasaCLient= APInasaClient(apiKey)
        self.data_transform= DataTransformer()
        self.asteroidService = AsteroidService(db_name)

    def run(self, start_date, end_date):
        try:
            print("getting the data from the API")
            apiData= self.apiNasaCLient.fetch_data(start_date, end_date)
            print("transform the data")
            transformedData= self.data_transform.transform(apiData)
            print("store the asteroids into the db")
            for asteroid in transformedData:
                self.asteroidService.insertAsteroids(asteroid)
            return self.asteroidService.find_5_largest_asteroids()
        except Exception as err:
            print('Creation failed: \nError: %s' % str(err))
        finally:
            self.asteroidService.closeDBconnection()
        