from analytics.query_executor import QueryExecutor
from analytics.query_library import QUERIES


class AnalyticsService:

    def __init__(self):

        self.executor = QueryExecutor()
    
    def apply_filters(self, sql, filters):
        if filters.get("gender") not in [None, "All"]:
            sql+= (
                f"\nAND GENDER = '{filters['gender']}'"
            )
        return sql

    def execute(
        self,
        section,
        query_name,
        filters = None,
    ):

        sql = QUERIES[section][query_name]

        if filters:
            sql = self.apply_filters(sql, filters)

        return self.executor.query(sql)

    def close(self):

        self.executor.close()