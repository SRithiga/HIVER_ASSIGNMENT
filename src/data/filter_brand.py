import pandas as pd
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[2]))
from config import RAW_DATA_PATH, FILTERED_BRAND_CSV, TARGET_BRAND, PROCESSED_DATA_DIR
from src.data.load_data import load_raw_dataset

def filter_brand_data(target_brand: str = TARGET_BRAND) -> pd.DataFrame:
    df = load_raw_dataset(RAW_DATA_PATH)
    PROCESSED_DATA_DIR.mkdir(parents=True, exist_ok=True)
    
    brand_outbound = df[(df['inbound'] == False) & (df['author_id'] == target_brand)]
    parent_ids = brand_outbound['in_response_to_tweet_id'].dropna().astype(int)
    customer_inbound = df[df['tweet_id'].isin(parent_ids)]
    
    filtered_df = pd.concat([brand_outbound, customer_inbound]).drop_duplicates(subset=['tweet_id'])
    filtered_df.to_csv(FILTERED_BRAND_CSV, index=False)
    
    print(f"Filtered {len(filtered_df):,} tweets for brand '{target_brand}'.")
    print(f"Saved to: {FILTERED_BRAND_CSV}")
    return filtered_df

if __name__ == "__main__":
    filter_brand_data()