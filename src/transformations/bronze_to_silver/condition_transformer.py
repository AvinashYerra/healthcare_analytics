from pyspark.sql.functions import current_timestamp

from transformations.base.base_transformer import BaseTransformer
from quality.data_quality import remove_duplicates


class ConditionTransformer(BaseTransformer):

    def clean(self, df):
        return remove_duplicates(df)

    def validate(self, df):
        return df

    def enrich(self, df):
        return df.withColumn(
            "processed_timestamp",
            current_timestamp(),
        )