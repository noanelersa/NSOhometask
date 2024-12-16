import sqlite3
from database.DBHandler import DBHandlerABC


class SQLiteDBHandler (DBHandlerABC):

    def __init__(self, name: str):
        self.name = name
        self.connection = sqlite3.connect(name)

    def createTable(self, dict) -> None:
        try:
            columns = ""
            for name, type in dict.items():
                columns += f"{name} {type} NOT NULL, \n"
            columns = columns.rstrip(", \n")
            cursor = self.connection.cursor()
            cursor.execute(f"DROP TABLE IF EXISTS {self.name}")
            cursor.execute(
                f"""CREATE TABLE IF NOT EXISTS {self.name} (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    {columns} )""")
            self.connection.commit()
        except Exception as err:
            print('Creation failed: \nError: %s' % str(err))
        finally:
            cursor.close()

    def insertData(self, data: dict) -> None:
        try:
            columns = ", ".join(data.keys())
            cursor = self.connection.cursor()
            placeholders = ", ".join("?" * len(data))
            query = f"""INSERT INTO {self.name}({columns})
            VALUES ({placeholders})"""
            cursor.execute(query, tuple(data.values()))
            self.connection.commit()
        except Exception as err:
            print('Insertion failed \nError: %s' % str(err))
        finally:
            cursor.close()

    def print_table(self) -> None:
        try:
            cursor = self.connection.cursor()
            cursor.execute(f"""SELECT * from {self.name}""")
            results = cursor.fetchall()
            for result in results:
                print(result)
        except Exception as err:
            print('Print failed \nError: %s' % str(err))
        finally:
            cursor.close()

    def readData(self, query: str, params=()):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            result = cursor.fetchall()
            return result
        except Exception as err:
            print('Read Query failed \nError: %s' % str(err))
        finally:
            cursor.close()

    def updateData(self, query: str, params) -> None:
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            self.connection.commit()
        except Exception as err:
            print('Update failed \nError: %s' % str(err))
        finally:
            cursor.close()

    def deleteData(self, query: str, params) -> None:
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            self.connection.commit()
        except Exception as err:
            print('Deletion failed \nError: %s' % str(err))
        finally:
            cursor.close()

    def close_connection(self):
        self.connection.close()
