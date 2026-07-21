from pathlib import Path

class BronzeReader:

    def __init__(self, spark):
        self.spark = spark

    def read(self, path, schema):

        path = str(Path(path))

        return (
            self.spark.read
            .schema(schema)
            .option("header", True)
            .csv(path)
        )