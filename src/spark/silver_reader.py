class SilverReader:

    def __init__(self, spark):
        self.spark = spark

    def read(self, path):
        return self.spark.read.parquet(str(path))