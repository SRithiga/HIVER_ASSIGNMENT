import pandas as pd
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[2]))
from config import FILTERED_BRAND_CSV, CONVERSATIONS_CSV, TARGET_BRAND

def build_pairs() -> pd.DataFrame:
    if not FILTERED_BRAND_CSV.exists():
        raise FileNotFoundError(f"Run filter_brand.py first. Missing {FILTERED_BRAND_CSV}")
    
    df = pd.read_csv(FILTERED_BRAND_CSV)
    brand_replies = df[(df['inbound'] == False) & (df['author_id'] == TARGET_BRAND)].copy()
    customer_tweets = df[df['inbound'] == True].copy()
    
    merged = pd.merge(
        brand_replies,
        customer_tweets,
        left_on='in_response_to_tweet_id',
        right_on='tweet_id',
        suffixes=('_brand', '_customer')
    )
    
    pairs = pd.DataFrame({
        'conversation_id': merged['tweet_id_customer'],
        'customer_tweet_id': merged['tweet_id_customer'],
        'customer_text': merged['text_customer'],
        'brand_tweet_id': merged['tweet_id_brand'],
        'brand_text': merged['text_brand'],
        'created_at': merged['created_at_customer']
    })
    
    pairs.to_csv(CONVERSATIONS_CSV, index=False)
    print(f"Constructed {len(pairs):,} Customer -> Brand conversation pairs.")
    print(f"Saved to: {CONVERSATIONS_CSV}")
    return pairs

if __name__ == "__main__":
    build_pairs()