from pyspark.sql.types import *

encounter_schema = StructType([
    StructField("Id", StringType(), True),
    StructField("START", TimestampType(), True),
    StructField("STOP", TimestampType(), True),
    StructField("PATIENT", StringType(), True),
    StructField("ORGANIZATION", StringType(), True),
    StructField("PROVIDER", StringType(), True),
    StructField("PAYER", StringType(), True),
    StructField("ENCOUNTERCLASS", StringType(), True),
    StructField("CODE", StringType(), True),
    StructField("DESCRIPTION", StringType(), True),
    StructField("BASE_ENCOUNTER_COST", DoubleType(), True),
    StructField("TOTAL_CLAIM_COST", DoubleType(), True),
    StructField("PAYER_COVERAGE", DoubleType(), True),
    StructField("REASONCODE", StringType(), True),
    StructField("REASONDESCRIPTION", StringType(), True)
])