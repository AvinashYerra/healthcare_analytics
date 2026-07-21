from time import time

from spark.session import create_spark_session
from spark.silver_reader import SilverReader
from spark.writer import ParquetWriter

from transformations.silver_to_gold.organization_summary_transformer import (
    OrganizationSummaryTransformer,
)
from common.pipeline_metrics import PipelineMetrics
from config.paths import OUTPUT_DIR


class OrganizationSummaryPipeline:

    def run(self):

        spark = create_spark_session(
            "Organization Summary Pipeline"
        )

        metrics = PipelineMetrics()

        reader = SilverReader(spark)
        writer = ParquetWriter()

        encounters = reader.read(
            OUTPUT_DIR / "silver/encounters"
        )

        organizations = reader.read(
            OUTPUT_DIR / "silver/organizations"
        )

        providers = reader.read(
            OUTPUT_DIR / "silver/providers"
        )


        metrics.input_records = organizations.count()

        transformer = OrganizationSummaryTransformer()

        summary = transformer.transform(
            organizations,
            providers,
            encounters,
        )

        metrics.output_records = summary.count()

        writer.write(
            summary,
            OUTPUT_DIR / "gold/organization_summary"
        )

        metrics.finish()

        metrics.report("organization_summary")

        # time.sleep(300) 
        spark.stop()