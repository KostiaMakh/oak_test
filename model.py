from db_connect import Db


class Model:
    """
    Class for creation table in MySQL DB
    """
    def __init__(self):
        self.db_connection = Db()
        self.table_name = self.__class__.__name__.lower()
        if not self._check_table():
            self._create_table()
            self._show_tables()
        else:
            print('Tabler already exists')

    def _create_table(self):
        self.db_connection.mycursor.execute(self._get_sql_query())

    def _get_sql_query(self):
        """
        Return sql query for creation table
        """
        query = f"CREATE TABLE {self.table_name} (id int NOT NULL AUTO_INCREMENT, "
        for param in self.__class__.__dict__.keys():
            if not param.startswith('__'):
                query += f'{param.lower()} {getattr(self, param).get_sql()}, '
        query += 'PRIMARY KEY (id))'
        return query

    def _show_tables(self):
        """
        Print already exists tables in db
        """
        self.db_connection.mycursor.execute("SHOW TABLES")

        for x in self.db_connection.mycursor:
            print(x)

    def _check_table(self) -> bool:
        """
        Check exists table or not
        """
        is_table_exists = False
        self.db_connection.mycursor.execute("SHOW TABLES")
        for db in self.db_connection.mycursor:
            if db[0] == self.table_name:
                is_table_exists = True
        return is_table_exists

    def all(self):
        """
        Returns all data from table
        """
        self.db_connection.mycursor.execute(f"SELECT * FROM {self.table_name}")
        all_objects = self.db_connection.mycursor.fetchall()

        return all_objects

    def create(self, *args, **kwargs):
        """
        :param kwargs: parameters of models
        """
        values = tuple(kwargs.values())
        sql = f"INSERT INTO {self.table_name} ({', '.join(list(kwargs.keys()))}) VALUES {values}"
        self.db_connection.mycursor.execute(sql)
        self.db_connection.mydb.commit()
