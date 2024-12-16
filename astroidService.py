from datetime import datetime, timedelta
from DBSQLightHandler import SQLightDBHandler
# this file takes care for the connection between the pipline and the asteroid DB

class AsteroidService():

    def __init__(self, db_name):
        self.dbHandler= SQLightDBHandler(db_name)
        self.dbHandler.createTable({
            'name': 'TEXT',
            'diameter': 'REAL',
            'approach_date': 'TEXT',
            'velocity': 'REAL'
        })
    def insertAsteroids(self, data):
        self.dbHandler.insertData(data)

    def find_5_largest_asteroids(self):
        today_date = datetime.today().strftime("%Y-%m-%d")
        end_date = (datetime.today() + datetime.timedelta(days=30)).strftime("%Y-%m-%d")
        params=(today_date,end_date)
        return self.dbHandler.readData("""SELECT name, diameter, approach_date, velocity
            FROM Asteroids
            WHERE approach_date BETWEEN ? AND ?
            ORDER BY diameter DESC
            LIMIT 5""", params)

    def closeDBconnection(self):
        self.dbHandler.close_connection()