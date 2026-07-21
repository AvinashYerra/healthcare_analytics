from spark.session import create_spark_session
from spark.bronze_reader import BronzeReader
from spark.writer import ParquetWriter
from common.pipeline_metrics import PipelineMetrics
from common.logger import get_logger



class GenericPipeline:

    def __init__(
        self,
        dataset_name,
        config,
    ):
        self.dataset_name = dataset_name
        self.config = config

    

    def run(self):
        schema = self.config["schema"]
        transformer = self.config["transformer"]
        input_path = self.config["bronze_path"]
        output_path = self.config["silver_path"]
        logger = get_logger(self.dataset_name)

        spark = create_spark_session(
            f"{self.dataset_name.title()} Pipeline"
        )

        metrics = PipelineMetrics()
        reader = BronzeReader(spark)
        writer = ParquetWriter()
        

        logger.info(f"Starting {self.dataset_name} pipeline")
        df = reader.read(
            input_path,
            schema,
        )

        metrics.input_records = df.count()
        logger.info(f"Input records : {metrics.input_records}")
        df = transformer.transform(df)
        logger.info(f"Output records : {metrics.output_records}")

        metrics.output_records = df.count()

        writer.write(
            df,
            output_path,
        )
        logger.info("Silver dataset written")
        metrics.finish()

        metrics.report(self.dataset_name)
        logger.info(f"{self.dataset_name} pipeline completed")
        spark.stop()