from abc import ABC, abstractmethod


class DBHandlerABC(ABC):
    @abstractmethod
    def createTable(self):
        raise NotImplementedError("Subclasses must implement 'createTable'")
        """Creates a table in the DB"""

    @abstractmethod
    def insertData(self, data: dict):
        raise NotImplementedError("Subclasses must implement 'insertData'")
        """Inserts data into the DB"""

    @abstractmethod
    def readData(self, query: str, params=()):
        raise NotImplementedError("Subclasses must implement 'readData'")
        """Reads data from the DB"""

    @abstractmethod
    def updateData(self, query: str, params):
        raise NotImplementedError("Subclasses must implement 'updateData'")
        """Updates data in the DB"""

    @abstractmethod
    def deleteData(self, query: str, params):
        raise NotImplementedError("Subclasses must implement 'deleteData'")
        """Deletes data from the DB"""
