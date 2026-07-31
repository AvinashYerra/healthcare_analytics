from pathlib import Path

from azure.identity import ClientSecretCredential
from azure.storage.filedatalake import DataLakeServiceClient

from ingestion.config import (
    STORAGE_ACCOUNT_NAME,
    FILE_SYSTEM_NAME,
    UPLOAD_DIRECTORY,
)
import os
from dotenv import load_dotenv

load_dotenv()


class AzureDataLakeUploader:
    def __init__(self):
        self.account_url = (
            f"https://{STORAGE_ACCOUNT_NAME}.dfs.core.windows.net"
        )

        self.credential = ClientSecretCredential(
            tenant_id=os.environ["AZURE_TENANT_ID"],
            client_id=os.environ["AZURE_CLIENT_ID"],
            client_secret=os.environ["AZURE_CLIENT_SECRET"],
        )


        self.service_client = DataLakeServiceClient(
            account_url=self.account_url,
            credential=self.credential,
        )

        self.file_system_client = self.service_client.get_file_system_client(
            FILE_SYSTEM_NAME
        )

    def upload_file(self, local_file: Path):
        destination = f"{UPLOAD_DIRECTORY}/{local_file.name}"

        print(f"Uploading {local_file.name}...")

        file_client = self.file_system_client.get_file_client(destination)

        with open(local_file, "rb") as data:
            file_client.upload_data(data, overwrite=True)

        print(f"Uploaded → {destination}")

    def upload_directory(self, files):
        uploaded = []
        failed = []

        for file in files:
            try:
                self.upload_file(file)
                uploaded.append(file.name)
            except Exception as ex:
                print(f"Failed: {file.name}")
                print(ex)
                failed.append(file.name)

        return uploaded, failed