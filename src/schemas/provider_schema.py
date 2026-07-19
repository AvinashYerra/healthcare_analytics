from pyspark.sql.types import (
    StructType,
    StructField,
    StringType,
    DoubleType,
)

provider_schema = StructType([
    StructField("Id", StringType(), True),
    StructField("ORGANIZATION", StringType(), True),
    StructField("NAME", StringType(), True),
    StructField("GENDER", StringType(), True),
    StructField("SPECIALITY", StringType(), True),
    StructField("ADDRESS", StringType(), True),
    StructField("CITY", StringType(), True),
    StructField("STATE", StringType(), True),
    StructField("ZIP", StringType(), True),
    StructField("LAT", DoubleType(), True),
    StructField("LON", DoubleType(), True),
])