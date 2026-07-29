import time
import json
from datetime import datetime
from config.paths import METRICS_DIR


class PipelineMetrics:

    def __init__(self):

        self.start_time = time.time()

        self.input_records = 0
        self.output_records = 0

        self.duplicates = 0
        self.null_primary_keys = 0

        self.status = "SUCCESS"

    def finish(self):

        self.execution_time = round(
            time.time() - self.start_time,
            2,
        )

    def report(self, dataset):

        print("\n" + "=" * 60)

        print(f"Dataset            : {dataset}")
        print(f"Status             : {self.status}")

        print(f"Input Records      : {self.input_records}")
        print(f"Output Records     : {self.output_records}")

        print(f"Duplicates         : {self.duplicates}")
        print(f"Null Primary Keys  : {self.null_primary_keys}")

        print(f"Execution Time     : {self.execution_time} sec")

        print("=" * 60)

    def save(
        self,
        dataset,
        layer,
    ):

        METRICS_DIR.mkdir(
            parents=True,
            exist_ok=True,
        )

        metrics = {

            "dataset": dataset,

            "layer": layer,

            "status": self.status,

            "input_records": self.input_records,

            "output_records": self.output_records,

            "duplicates": self.duplicates,

            "null_primary_keys": self.null_primary_keys,

            "execution_time": self.execution_time,

            "timestamp": datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),
        }

        with open(
            METRICS_DIR / f"{dataset}.json",
            "w",
        ) as f:

            json.dump(
                metrics,
                f,
                indent=4,
            )