from DBSQLightHandler import SQLightDBHandler
from api_nasa_client import APInasaClient
from pipline import Pipline

def mainA():

    start = Pipline('atGTDOlBIj4CkCcWdEpTTJfQ3okIe5kBnkgRpB0N', 'Asteroids')
    start.run('2024-12-20', '2024-12-22')
    


    """sqlightDB = SQLightDBHandler("Asteroids")
    sqlightDB.createTable({'name':'TEXT', 'diameter':'REAL', 'approach_date':'TEXT', 'velocity':'REAL'})
    sqlightDB.insertData({
        'name': 'Asteroid1',
        'diameter': 1000.5,
        'approach_date': '2024-12-15',
        'velocity': 20.45
    })
    sqlightDB.insertData({
        'name': 'Asteroid2',
        'diameter': 1001.1,
        'approach_date': '2024-12-16',
        'velocity': 20.46
    })
    #sqlightDB.deleteData("DELETE FROM Asteroids WHERE name = ?", ('Asteroid1',))
    #sqlightDB.print_table()
    sqlightDB.readData("SELECT * FROM Asteroids")
    sqlightDB.updateData( "UPDATE Asteroids SET diameter = ?, velocity = ? WHERE name = ?", (1500.5, 25.75, 'Asteroid1'))
    sqlightDB.print_table()
    

    #api_key = "atGTDOlBIj4CkCcWdEpTTJfQ3okIe5kBnkgRpB0N"
    #nasa_client = APInasaClient(api_key)
    #data = nasa_client.fetch_data("2024-12-15", "2024-12-22")
    #print(data)"""


if __name__=='__main__':
    mainA()
