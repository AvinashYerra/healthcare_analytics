from pathlib import Path
from datetime import datetime

# Azure
STORAGE_ACCOUNT_NAME = "sthcplatdev01"
FILE_SYSTEM_NAME = "bronze"

# Local Dataset
LOCAL_DATASET_PATH = Path.home()/"open source" / "synthea" / "output" / "csv"

# Dataset Metadata
SOURCE_NAME = "synthea"
SOURCE_VERSION = "v1"

today = datetime.today()

UPLOAD_DIRECTORY = (
    f"source={SOURCE_NAME}/"
    f"version={SOURCE_VERSION}/"
    f"ingestion_date={today.strftime('%Y-%m-%d')}"
)
