from pyspark.sql.types import *

condition_schema = StructType([
    StructField("START", DateType(), True),
    StructField("STOP", DateType(), True),
    StructField("PATIENT", StringType(), True),
    StructField("ENCOUNTER", StringType(), True),
    StructField("SYSTEM", StringType(), True),
    StructField("CODE", StringType(), True),
    StructField("DESCRIPTION", StringType(), True),
])