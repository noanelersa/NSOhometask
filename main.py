from database.DBSQLiteHandler import SQLiteDBHandler
from pipelines.pipeline import Pipeline
from config import API_KEY, DB_NAME, START_DATE, END_DATE


def main():
    dbHandler = SQLiteDBHandler(DB_NAME)
    dbHandler.createTable({
        'name': 'TEXT',
        'diameter': 'REAL',
        'approachDate': 'TEXT',
        'velocity': 'REAL'
    })
    start = Pipeline(API_KEY, DB_NAME)
    start.run(START_DATE, END_DATE)

if __name__ == '__main__':
    main()
