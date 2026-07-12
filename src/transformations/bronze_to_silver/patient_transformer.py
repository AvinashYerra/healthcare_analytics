from pyspark.sql import DataFrame
from pyspark.sql.functions import current_timestamp

from transformations.base.base_transformer import BaseTransformer

from quality.data_quality import (
    remove_duplicates,
    remove_null_primary_keys,
)


class PatientTransformer(BaseTransformer):

    def clean(self, df: DataFrame):
        df = remove_duplicates(df)
        return df

    def validate(self, df: DataFrame):
        df = remove_null_primary_keys(df, "Id")
        return df

    def enrich(self, df: DataFrame):
        return df.withColumn(
            "processed_timestamp",
            current_timestamp(),
        )