"""
Definition of Column:
class Column:
    def __init__(self, key, value):
        self.key = key
        self.value = value
"""


class MiniCassandra:
    
    def __init__(self):
        """
        initialize an empty hash table
        {(row_key, column_key): value}
        """
        self.hash = {}

    def insert(self, row_key, column_key, value):
        """
        @param: row_key: a string
        @param: column_key: An integer
        @param: value: a string
        @return: nothing
        """
        self.hash[(row_key, column_key)] = value

    
    def query(self, row_key, column_start, column_end):
        """
        @param: row_key: a string
        @param: column_start: An integer
        @param: column_end: An integer
        @return: a list of Columns
        """
        output = []
        for row, col in sorted(self.hash):
            if row == row_key and col >= column_start and col <= column_end:
                output.append(Column(col, self.hash[(row, col)]))  #################
        return output
