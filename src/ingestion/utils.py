from pathlib import Path

def get_csv_files(directory: Path):
    """
    Returns all CSV files from the given directory.
    """
    return sorted(directory.glob("*.csv"))