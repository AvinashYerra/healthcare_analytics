from pathlib import Path
from pyspark.sql import DataFrame


class SilverWriter:

    def write(self, df: DataFrame, path):

        path = str(Path(path))

        (
            df.write
            .mode("overwrite")
            .parquet(path)
        )