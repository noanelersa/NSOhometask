import sqlite3
import DBHandler

class SQLightDBHandler (DBHandler):

    def __init__(self, name):
        self.name= name
        self.connection= sqlite3.connect(name)
        self.cursor = self.connection.cursor()

   # def createTable(self):
       # self.cursor.execute().....