from mysql.connector import connect
import settings


class Db:
    """
    Class for connection for db
    """
    def __init__(self):
        self.mydb = connect(
            host=settings.SQL_HOST,
            user=settings.SQL_USER,
            password=settings.SQL_PASSWORD,
            database=settings.SQL_DB_NAME
        )
        self.mycursor = self.mydb.cursor()
    #     self.create_db(settings.SQL_DB_NAME)
    #
    # def create_db(self, db_name: str):
    #     """
    #     Create database
    #     """
    #     if not self.check_db(db_name):
    #         self.mycursor.execute(f"CREATE DATABASE {db_name}")
    #         print(f'db {db_name} successfully created')
    #     else:
    #         print(f'{db_name} DB already exists')
    #
    # def check_db(self, db_name: str) -> bool:
    #     """
    #     Check exists db or not
    #     """
    #     is_db_exists = False
    #     self.mycursor.execute("SHOW DATABASES")
    #     for db in self.mycursor:
    #         if db[0] == db_name.lower():
    #             is_db_exists = True
    #     return is_db_exists
