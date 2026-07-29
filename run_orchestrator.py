import time

from pipelines.run_pipeline import run_pipeline

from config.dataset_registry import DATASETS
from config.summary_registry import SUMMARIES

from common.logger import get_logger

from storage.deployment import DEPLOYMENT
from storage.uploader import AzureUploader
from config.dataset_registry import DATASETS  
from config.summary_registry import SUMMARIES


def run_bronze_to_silver():

    logger = get_logger("bronze_to_silver")

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

    return successful, failed


def upload_silver():

    if not DEPLOYMENT["azure"]["silver"]:
        return

    logger = get_logger("silver_upload")

    print("\nUploading Silver Layer to Azure...\n")

    uploader = AzureUploader()

    for dataset, config in DATASETS.items():

        logger.info(f"Uploading {dataset}")

        uploader.upload_directory(
            config["output_path"],
            "silver",
            dataset,
        )


def run_silver_to_gold():

    logger = get_logger("silver_to_gold")

    successful = 0
    failed = []

    print("\nRunning Silver → Gold Pipelines...\n")

    for summary_name, config in SUMMARIES.items():

        logger.info(f"Running {summary_name} pipeline...")

        try:

            config["pipeline"].run()
            successful += 1

        except Exception as e:

            logger.exception(e)
            failed.append(summary_name)

    return successful, failed


def upload_gold():

    if not DEPLOYMENT["azure"]["gold"]:
        return

    logger = get_logger("gold_upload")

    print("\nUploading Gold Layer to Azure...\n")

    uploader = AzureUploader()

    for summary_name, config in SUMMARIES.items():

        logger.info(f"Uploading {summary_name}")

        uploader.upload_directory(
            local_directory=config["output_path"],
            container="gold",
            dataset=summary_name,
        )


def main():

    start = time.time()

    print("\n" + "=" * 60)
    print("Healthcare Analytics ETL")
    print("=" * 60)

    successful = 0
    failed = []

    success, errors = run_bronze_to_silver()
    successful += success
    failed.extend(errors)

    upload_silver()

    success, errors = run_silver_to_gold()
    successful += success
    failed.extend(errors)

    upload_gold()

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

if __name__ == "__main__": main()