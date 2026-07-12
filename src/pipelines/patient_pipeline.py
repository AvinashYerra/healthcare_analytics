from spark.session import create_spark_session
from spark.BronzeReader import BronzeReader
from spark.SilverWriter import SilverWriter
from src.common.pipeline_metrics import PipelineMetrics
from quality.data_quality import duplicate_count, null_count

from schemas.patient_schema import patient_schema

from transformations.bronze_to_silver.patient_transformer import (
    PatientTransformer,
)

from config.paths import (
    SAMPLE_DATA_DIR,
    SILVER_DIR,
)


def main():

    spark = create_spark_session()
    reader = BronzeReader(spark)
    writer = SilverWriter()
    transformer = PatientTransformer()

    df = reader.read(
        SAMPLE_DATA_DIR / "patients.csv",
        patient_schema,
    )

    metrics = PipelineMetrics()
    metrics.input_records = df.count()
    metrics.duplicates = duplicate_count(df)
    metrics.null_primary_keys = null_count(df, "Id")
    df = transformer.transform(df)
    metrics.output_records = df.count()
    metrics.finish()
    metrics.report("patients")

    writer.write(
        df,
        SILVER_DIR / "patients",
    )

    spark.stop()


if __name__ == "__main__":
    main()