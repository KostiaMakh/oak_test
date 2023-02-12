
class CharField:
    """
    Class for creation integer field in db
    """
    def __init__(self, max_length: int):
        self.type = 'VARCHAR'
        self.max_length = max_length

    def get_sql(self):
        """
        returns sql query for creation column
        """
        return f'{self.type} ({self.max_length})'


class IntegerField:
    """
    Class for creation integer field in db
    """
    def __init__(self, default: int = 0):
        self.type = 'INT'
        self.default = default

    def get_sql(self):
        """
        returns sql query for creation column
        """
        return f'{self.type} ({self.default})'
