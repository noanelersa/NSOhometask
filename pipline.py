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
            
            apiData= self.apiNasaCLient.fetch_data(start_date, end_date)
            print("got the data from the API")
            
            transformedData= self.data_transform.transform(apiData)
            print("transformed the data")
            
            for asteroid in transformedData:
                self.asteroidService.insertAsteroids(asteroid)
            print("stored the asteroids into the db")

            print( "the 5 largest asteroids by diameter are:")
            print(self.asteroidService.find_5_largest_asteroids())
        except Exception as err:
            print('Creation failed: \nError: %s' % str(err))
        finally:
            self.asteroidService.closeDBconnection()
        