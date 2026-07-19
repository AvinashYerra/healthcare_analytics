import time

from run_pipeline import run_pipeline
from config.dataset_registry import DATASETS
from common.logger import get_logger


def main():


    start = time.time()
    logger = get_logger("orchestrator")
    print("\n" + "=" * 60)
    print("Healthcare Analytics ETL")
    print("=" * 60)

    successful = 0
    failed = []

    for dataset in DATASETS.keys():

        logger.info(f"Running {dataset} pipeline...")

        try:
            run_pipeline(dataset)
            successful += 1

        except Exception as e:

            print(f"FAILED : {dataset}")
            logger.exception(e)
            failed.append(dataset)

    elapsed = round(time.time() - start, 2)

    print("\n" + "=" * 60)
    print("Execution Summary")
    print("=" * 60)
    print(f"Successful Pipelines : {successful}")
    print(f"Failed Pipelines     : {len(failed)}")
    print(f"Execution Time       : {elapsed} sec")

    if failed:
        print("\nFailed Pipelines:")
        for dataset in failed:
            print(f" - {dataset}")

    print("=" * 60)


if __name__ == "__main__":
    main()