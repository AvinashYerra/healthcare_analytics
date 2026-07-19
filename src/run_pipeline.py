import sys

from config.datasets import DATASETS
from config.transformers import TRANSFORMERS

from spark.session import create_spark_session as get_spark
from spark.BronzeReader import BronzeReader
from spark.SilverWriter import SilverWriter

from pipelines.base_pipeline import BasePipeline


def main():

    if len(sys.argv) != 2:
        print("Usage:")
        print("python src/run_pipeline.py patients")
        return

    dataset = sys.argv[1].lower()

    if dataset not in DATASETS:
        raise ValueError(f"Unknown dataset: {dataset}")

    spark = get_spark()

    pipeline = BasePipeline(
        reader=BronzeReader(spark),
        writer=SilverWriter(),
        transformer=TRANSFORMERS[dataset](),
    )

    pipeline.execute(DATASETS[dataset])


if __name__ == "__main__":
    main()