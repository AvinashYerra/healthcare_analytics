from pyspark.sql import DataFrame
from pyspark.sql.functions import (
    col,
    current_timestamp,
    trim,
    upper,
    regexp_replace,
)

from transformations.base.base_transformer import BaseTransformer

from quality.data_quality import (
    remove_duplicates,
    remove_nulls,
)


class OrganizationTransformer(BaseTransformer):

    def clean(self, df: DataFrame):

        df = remove_duplicates(df)

        df = remove_nulls(df, "Id")

        return df

    def validate(self, df: DataFrame):

        return df

    def enrich(self, df: DataFrame):

        return (
            df

            .withColumn(
                "NAME",
                trim(col("NAME"))
            )

            .withColumn(
                "ADDRESS",
                trim(col("ADDRESS"))
            )

            .withColumn(
                "CITY",
                trim(col("CITY"))
            )

            .withColumn(
                "STATE",
                upper(trim(col("STATE")))
            )

            .withColumn(
                "ZIP",
                regexp_replace(col("ZIP"), "-", "")
            )

            .withColumn(
                "processed_timestamp",
                current_timestamp()
            )
        )