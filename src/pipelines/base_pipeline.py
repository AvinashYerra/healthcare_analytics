from common.pipeline_metrics import PipelineMetrics
from quality.data_quality import duplicate_count, null_count


class BasePipeline:

    def __init__(self, reader, writer, transformer):
        self.reader = reader
        self.writer = writer
        self.transformer = transformer

    def execute(self, config):

        metrics = PipelineMetrics()
        print(f"\nRunning pipeline for {config['dataset']}")

        # Read
        df = self.reader.read(
            config["input_path"],
            config["schema"]
        )

        metrics.input_records = df.count()

        # Data Quality
        metrics.duplicates = duplicate_count(df)
        metrics.null_primary_keys = null_count(
            df,
            config["primary_key"]
        )

        # Transform
        df = self.transformer.transform(df)
        metrics.output_records = df.count()

        # Write
        self.writer.write(
            df,
            config["output_path"]
        )

        metrics.finish()
        metrics.report(config["dataset"])