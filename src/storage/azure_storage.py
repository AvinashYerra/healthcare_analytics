from azure.identity import ClientSecretCredential
from azure.storage.filedatalake import DataLakeServiceClient

from config.azure import (
    STORAGE_ACCOUNT_NAME,
    CONTAINERS,
)
import os
from dotenv import load_dotenv

load_dotenv()

class AzureStorage:

    def __init__(self):

        account_url = (
            f"https://{STORAGE_ACCOUNT_NAME}.dfs.core.windows.net"
        )
        self.credential = ClientSecretCredential(
                    tenant_id=os.environ["AZURE_TENANT_ID"],
                    client_id=os.environ["AZURE_CLIENT_ID"],
                    client_secret=os.environ["AZURE_CLIENT_SECRET"],
                )
        
        self.service = DataLakeServiceClient(
            account_url=account_url,
            credential=self.credential,
        )

    def get_container(self, layer):

        return self.service.get_file_system_client(
            CONTAINERS[layer]
        )