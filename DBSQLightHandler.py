import sqlite3
import DBHandler

class SQLightDBHandler (DBHandler):

    def __init__(self, name):
        self.name= name
        self.connection= sqlite3.connect(name)
        self.cursor = self.connection.cursor()

    def createTable(self):
        try:
            self.cursor.execute(
                """CREATE TABLE IF NOT EXISTS Asteroids (
                    name TEXT PRIMARY KEY,
                    diameter REAL NOT NULL,
                    approach_date TEXT NOT NULL,
                    velocity REAL NOT NULL )""")     
        #except sqlite3.   ???????

        finally:
            self.connection.commit()
            self.cursor.close()
    
    def insertData(self, data):
        try:
            self.cursor.execute(
            """INSERT INTO Asteroids(name, diameter, approach_date,velocity) 
            VALUES (?, ?, ?, ?)""",
            data['name'],data['diameter'], data['approach_data'],data['velocity']
        )
        #except sqlite3.  ??????????
        finally:
            self.connection.commit()
            self.cursor.close()

    
    def readData(self, query, params=()):
        self.cursor.execute(query, params)
        result = self.cursor.fetchall()
        self.connection.commit()
        self.cursor.close()
        
    
    def updateData(self, query, params):
        self.cursor.execute(query,params)
        self.connection.commit()
        self.cursor.close()

    def deleteData(self, query, params):
        self.cursor.execute(query,params)
        self.connection.commit()
        self.cursor.close()

    def close_connection (self):
        self.connection.close()
    


 

       