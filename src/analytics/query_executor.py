from analytics.analytics_registry import ANALYTICS
from analytics.duckdb_manager import DuckDBManager


class QueryExecutor:

    def __init__(self):

        self.db = DuckDBManager()

        self.register_views()

    def register_views(self):

        for config in ANALYTICS.values():

            self.db.execute(f"""
                CREATE OR REPLACE VIEW {config["table"]} AS
                SELECT *
                FROM read_parquet('{config["path"]}/*.parquet')
            """)

    def query(self, sql):

        return self.db.dataframe(sql)

    def close(self):

        self.db.close()