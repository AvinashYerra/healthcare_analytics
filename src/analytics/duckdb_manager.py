import duckdb


class DuckDBManager:

    def __init__(self):

        self.connection = duckdb.connect()

    def execute(
        self,
        query,
    ):

        return self.connection.execute(query)

    def dataframe(
        self,
        query,
    ):

        return self.connection.execute(query).df()

    def close(self):

        self.connection.close()