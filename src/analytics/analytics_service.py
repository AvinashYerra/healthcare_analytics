from analytics.query_executor import QueryExecutor
from analytics.query_library import QUERIES


class AnalyticsService:

    def __init__(self):

        self.executor = QueryExecutor()

    def execute(
        self,
        section,
        query_name,
    ):

        sql = QUERIES[section][query_name]

        return self.executor.query(sql)

    def close(self):

        self.executor.close()