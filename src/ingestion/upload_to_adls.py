from ingestion.config import LOCAL_DATASET_PATH
from ingestion.uploader import AzureDataLakeUploader
from ingestion.utils import get_csv_files


def main():

    print("=" * 60)
    print("Healthcare Bronze Layer Ingestion")
    print("=" * 60)

    csv_files = get_csv_files(LOCAL_DATASET_PATH)

    print(f"\nFound {len(csv_files)} CSV files\n")

    uploader = AzureDataLakeUploader()

    # uploader.upload_directory(csv_files)
    uploaded, failed = uploader.upload_directory(csv_files)

    print("\n" + "=" * 60)
    print("Upload Summary")
    print("=" * 60)

    print(f"Uploaded : {len(uploaded)}")
    print(f"Failed   : {len(failed)}")

    if failed:
        print("\nFailed Files:")
        for file in failed:
            print(f" - {file}")

    print("\nUpload Completed Successfully!")


if __name__ == "__main__":
    main()