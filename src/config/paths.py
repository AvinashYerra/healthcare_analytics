from datetime import datetime
from pathlib import Path
from config.settings import (
    SOURCE_NAME,
    SOURCE_VERSION,
)


PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATA_DIR = PROJECT_ROOT / "data"

SAMPLE_DATA_DIR = DATA_DIR / "sample" / "csv"

SCHEMA_DIR = DATA_DIR / "schemas"

OUTPUT_DIR = DATA_DIR / "output"

SILVER_DIR = OUTPUT_DIR / "silver"

GOLD_DIR = OUTPUT_DIR / "gold"


today = datetime.today()

INGESTION_DATE = today.strftime("%Y-%m-%d")


def bronze_dataset_path(dataset_name: str):

    return (
        f"source={SOURCE_NAME}/"
        f"version={SOURCE_VERSION}/"
        f"ingestion_date={INGESTION_DATE}/"
        f"{dataset_name}.csv"
    )
