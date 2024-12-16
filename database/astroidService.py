from datetime import datetime, timedelta
from database.DBSQLiteHandler import SQLiteDBHandler
from config import DATE_FORMAT, ASTEROID_LIMIT

# this file takes care for the connection between the pipline and the asteroid DB


class AsteroidService:

    def __init__(self, db_name: str):
        self.dbHandler = SQLiteDBHandler(db_name)

    def insert_asteroids(self, data: dict) -> None:
        self.dbHandler.insertData(data)

    def find_5_largest_asteroids(self) -> list:
        today_date = datetime.today().strftime(DATE_FORMAT)
        end_date = (datetime.today() + timedelta(days=30)
                    ).strftime(DATE_FORMAT)
        params = (today_date, end_date)
        result = self.dbHandler.readData(f"""SELECT name, diameter, approachDate, velocity
            FROM Asteroids
            WHERE approachDate BETWEEN ? AND ?
            ORDER BY diameter DESC
            LIMIT {ASTEROID_LIMIT}""", params)
        return result

    def closeDBconnection(self) -> None:
        self.dbHandler.close_connection()
