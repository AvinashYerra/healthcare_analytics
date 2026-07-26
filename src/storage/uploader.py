from pathlib import Path

from storage.azure_storage import AzureStorage
from common.logger import get_logger

class AzureUploader:

    def __init__(self):

        self.storage = AzureStorage()

    def upload_directory(
        self,
        local_directory,
        container,
        dataset,
    ):
        logger = get_logger("azure_uploader")
        local_directory = Path(local_directory)

        file_system = self.storage.get_container(container)

        uploaded = 0

        for file in local_directory.iterdir():

            if not file.is_file():
                continue
            if file.name.endswith(".crc"):
                continue
            if file.name.startswith("."):
                continue

            remote_path = f"{dataset}/{file.name}"
            logger.info(f"Uploading {remote_path}")

            file_client = file_system.get_file_client(
                remote_path
            )

            with open(file, "rb") as data:

                file_client.upload_data(
                    data,
                    overwrite=True,
                )

            uploaded += 1

        logger.info(f"Finished uploading {uploaded} files to {container}/{dataset}")