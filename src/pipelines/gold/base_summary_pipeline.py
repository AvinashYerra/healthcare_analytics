from spark.session import create_spark_session
from spark.silver_reader import SilverReader
from spark.writer import ParquetWriter

from common.pipeline_metrics import PipelineMetrics
from common.logger import get_logger


class BaseSummaryPipeline:

    def __init__(self, pipeline_name, output_path):

        self.pipeline_name = pipeline_name
        self.output_path = output_path

    def run(self):

        spark = create_spark_session(
            self.pipeline_name.replace("_", " ").title()
        )

        logger = get_logger(self.pipeline_name)

        metrics = PipelineMetrics()

        reader = SilverReader(spark)
        writer = ParquetWriter()

        logger.info(f"Starting {self.pipeline_name}")

        summary = self.build_summary(
            reader,
            metrics,
        )

        metrics.output_records = summary.count()

        writer.write(
            summary,
            self.output_path,
        )

        logger.info("Gold dataset written")

        metrics.finish()
        metrics.report(self.pipeline_name)

        logger.info(f"{self.pipeline_name} completed")

        spark.stop()

    def build_summary(
        self,
        reader,
        metrics,
    ):
        raise NotImplementedError