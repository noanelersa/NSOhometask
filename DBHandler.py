from abc import ABC, abstractmethod

class DatabaseHandlerInterface(ABC):
    @abstractmethod
    def createTable(self):
        raise NotImplementedError("Subclasses must implement 'createTable'")
        """Creates a table in the DB"""

    @abstractmethod
    def insertData(self, data):
        raise NotImplementedError("Subclasses must implement 'insertData'")
        """Inserts data into the DB"""

    @abstractmethod
    def readData(self, query, params=()):
        raise NotImplementedError("Subclasses must implement 'readData'")
        """Reads data from the DB"""

    @abstractmethod
    def updateData(self, query, params):
        raise NotImplementedError("Subclasses must implement 'updateData'")
        """Updates data in the DB"""

    @abstractmethod
    def deleteData(self, query, params):
        raise NotImplementedError("Subclasses must implement 'deleteData'")
        """Deletes data from the DB"""


