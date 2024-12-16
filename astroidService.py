from datetime import datetime, timedelta
from DBSQLightHandler import SQLightDBHandler
# this file takes care for the connection between the pipline and the asteroid DB

class AsteroidService():

    def __init__(self, db_name):
        self.dbHandler= SQLightDBHandler(db_name)
        self.dbHandler.createTable({
            'name': 'TEXT',
            'diameter': 'REAL',
            'approachDate': 'TEXT',
            'velocity': 'REAL'
        })
    def insertAsteroids(self, data):
        self.dbHandler.insertData(data)

    def find_5_largest_asteroids(self):
        today_date = datetime.today().strftime("%Y-%m-%d")
        end_date = (datetime.today() + timedelta(days=30)).strftime("%Y-%m-%d")
        params=(today_date,end_date)
        
        result= self.dbHandler.readData(f"""SELECT name, diameter, approachDate, velocity
            FROM Asteroids
            WHERE approachDate BETWEEN ? AND ?
            ORDER BY diameter DESC
            LIMIT 5""", params)
        return result

    def closeDBconnection(self):
        self.dbHandler.close_connection()