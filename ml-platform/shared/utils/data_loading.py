from pathlib import Path
from typing import Optional
import pandas as pd
import duckdb


def get_csv_path(filename: str, data_dir: Optional[Path] = None) -> Path:
    """
    Returns the full path to a CSV file in the data/raw directory.
    """
    if data_dir is None:
        project_root = Path.cwd() if (Path.cwd() / 'data').exists() else Path.cwd().parent
        data_dir = project_root / 'data' / 'raw'
    return data_dir / filename

def load_csv(filename: str, **kwargs) -> Optional[pd.DataFrame]:
    """
    Loads a CSV file from the data/raw directory using pandas.
    Returns a DataFrame or None if loading fails.
    """
    csv_path = get_csv_path(filename)
    try:
        df = pd.read_csv(csv_path, **kwargs)
        print(f"✅ CSV loaded successfully: {csv_path}")
        return df
    except FileNotFoundError:
        print(f"❌ File not found: {csv_path}")
    except Exception as e:
        print(f"❌ Failed to load CSV: {e}")
    return None

def duckdb_read_csv(filename: str, delim: str = ';', decimal_separator: str = ',', nullstr: str = ' ', **kwargs) -> Optional[pd.DataFrame]:
    """
    Loads a CSV file using DuckDB's read_csv_auto.
    Returns a DataFrame or None if loading fails.
    """
    csv_path = get_csv_path(filename)
    query = f"""
    SELECT * FROM read_csv_auto(
        '{csv_path.as_posix()}',
        delim='{delim}',
        decimal_separator='{decimal_separator}',
        nullstr='{nullstr}'
    )
    """
    try:
        return duckdb.query(query).to_df()
    except Exception as e:
        print(f"❌ DuckDB failed to load {filename}: {e}")
        return None

def list_csv_files(data_dir: Optional[Path] = None):
    """
    Lists all CSV files in the data/raw directory.
    """
    if data_dir is None:
        project_root = Path.cwd() if (Path.cwd() / 'data').exists() else Path.cwd().parent
        data_dir = project_root / 'data' / 'raw'
    return [f.name for f in data_dir.glob('*.csv')]