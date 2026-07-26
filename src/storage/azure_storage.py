from azure.identity import DefaultAzureCredential
from azure.storage.filedatalake import DataLakeServiceClient

from config.azure import (
    STORAGE_ACCOUNT_NAME,
    CONTAINERS,
)


class AzureStorage:

    def __init__(self):

        account_url = (
            f"https://{STORAGE_ACCOUNT_NAME}.dfs.core.windows.net"
        )

        self.service = DataLakeServiceClient(
            account_url=account_url,
            credential=DefaultAzureCredential(),
        )

    def get_container(self, layer):

        return self.service.get_file_system_client(
            CONTAINERS[layer]
        )