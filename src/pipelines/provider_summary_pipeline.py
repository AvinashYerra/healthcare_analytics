import time

from spark.session import create_spark_session
from spark.silver_reader import SilverReader
from spark.writer import ParquetWriter
from common.pipeline_metrics import PipelineMetrics
from config.paths import OUTPUT_DIR
from transformations.silver_to_gold.provider_summary_transformer import ProviderSummaryTransformer


class ProviderSummaryPipeline:

    def run(self):

        spark = create_spark_session(
            "Provider Summary Pipeline"
        )

        metrics = PipelineMetrics()

        reader = SilverReader(spark)
        writer = ParquetWriter()

        providers = reader.read(
            OUTPUT_DIR / "silver/providers"
        )

        encounters = reader.read(
            OUTPUT_DIR / "silver/encounters"
        )

        conditions = reader.read(
            OUTPUT_DIR / "silver/conditions"
        )

        metrics.input_records = providers.count()

        transformer = ProviderSummaryTransformer()

        summary = transformer.transform(
            providers,
            encounters,
        )

        metrics.output_records = summary.count()

        writer.write(
            summary,
            OUTPUT_DIR / "gold/provider_summary"
        )

        metrics.finish()

        metrics.report("provider_summary")
        # time.sleep(300) 
        spark.stop()