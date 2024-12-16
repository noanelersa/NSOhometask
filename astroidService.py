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

    def closeDBconnection(self):
        self.dbHandler.close_connection()