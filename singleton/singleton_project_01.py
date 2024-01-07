import sqlite3

class MetaDatabaseSingleton(type):
    
    __instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instance:
            cls.__instance[cls] = super(MetaDatabaseSingleton, cls).__call__(*args, **kwargs)
        return cls.__instance[cls]
    
# MetaDatabaseSingleton irá controlar para que haja
# Apenas uma instância da classe Database
class Database(metaclass=MetaDatabaseSingleton):
    
    connection = None

    def connect(self):

        if self.connection is None:
            print(f"Criando uma conexão com o banco de dados...")
            self.connection = sqlite3.connect('db.sqlite')
            self.cursor = self.connection.cursor()

        return self.cursor
    
database_1 = Database().connect()
database_2 = Database().connect()

