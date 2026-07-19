from pyspark.sql import DataFrame
from pyspark.sql.functions import current_timestamp

from transformations.base.base_transformer import BaseTransformer
from quality.data_quality import (
    remove_duplicates,
    remove_nulls,
)


class ProviderTransformer(BaseTransformer):

    def clean(self, df: DataFrame):

        return remove_duplicates(df)

    def validate(self, df: DataFrame):

        return remove_nulls(df, "Id")

    def enrich(self, df: DataFrame):

        return df.withColumn(
            "processed_timestamp",
            current_timestamp(),
        )