from abc import ABC, abstractmethod
from pyspark.sql import DataFrame


class BaseTransformer(ABC):

    def transform(self, df: DataFrame) -> DataFrame:
        """
        Executes the transformation pipeline.
        """

        df = self.clean(df)
        df = self.validate(df)
        df = self.enrich(df)

        return df

    @abstractmethod
    def clean(self, df: DataFrame) -> DataFrame:
        pass

    @abstractmethod
    def validate(self, df: DataFrame) -> DataFrame:
        pass

    @abstractmethod
    def enrich(self, df: DataFrame) -> DataFrame:
        pass