import time

from pipelines.run_pipeline import run_pipeline

from config.dataset_registry import DATASETS
from config.summary_registry import SUMMARIES

from common.logger import get_logger


def main():

    start = time.time()

    logger = get_logger("orchestrator")

    print("\n" + "=" * 60)
    print("Healthcare Analytics ETL")
    print("=" * 60)

    successful = 0
    failed = []


    print("\nRunning Bronze → Silver Pipelines...\n")

    for dataset in DATASETS.keys():

        logger.info(f"Running {dataset} pipeline...")

        try:

            run_pipeline(dataset)
            successful += 1

        except Exception as e:

            logger.exception(e)
            failed.append(dataset)



    print("\nRunning Silver → Gold Pipelines...\n")

    for summary_name, pipeline in SUMMARIES.items():

        logger.info(f"Running {summary_name} pipeline...")

        try:

            pipeline.run()
            successful += 1

        except Exception as e:

            logger.exception(e)
            failed.append(summary_name)

    elapsed = round(time.time() - start, 2)

    print("\n" + "=" * 60)
    print("Execution Summary")
    print("=" * 60)
    print(f"Successful Pipelines : {successful}")
    print(f"Failed Pipelines     : {len(failed)}")
    print(f"Execution Time       : {elapsed} sec")

    if failed:

        print("\nFailed Pipelines:")

        for pipeline in failed:
            print(f" - {pipeline}")

    print("=" * 60)


if __name__ == "__main__":
    main()