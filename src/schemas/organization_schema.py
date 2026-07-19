from pyspark.sql.types import *

organization_schema = StructType([

    StructField("Id", StringType(), True),

    StructField("NAME", StringType(), True),

    StructField("ADDRESS", StringType(), True),

    StructField("CITY", StringType(), True),

    StructField("STATE", StringType(), True),

    StructField("ZIP", StringType(), True),

    StructField("LAT", DoubleType(), True),

    StructField("LON", DoubleType(), True),

    StructField("PHONE", StringType(), True),

    StructField("REVENUE", DoubleType(), True),

    StructField("UTILIZATION", IntegerType(), True),
])