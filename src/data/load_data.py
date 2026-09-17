import pandas as pd
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[2]))
from config import RAW_DATA_PATH

def load_raw_dataset(path: Path = RAW_DATA_PATH) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(f"Dataset file missing at {path}")
    print(f"Loading raw dataset from {path}...")
    df = pd.read_csv(path)
    print(f"Successfully loaded {len(df):,} rows.")
    return df

if __name__ == "__main__":
    df = load_raw_dataset()