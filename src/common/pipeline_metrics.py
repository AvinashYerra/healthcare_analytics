import time


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