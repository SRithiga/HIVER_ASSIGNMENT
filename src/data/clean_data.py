import pandas as pd
import re
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[2]))
from config import CONVERSATIONS_CSV, CLEANED_CONVERSATIONS_CSV

def clean_tweet_text(text: str) -> str:
    if not isinstance(text, str):
        return ""
    text = re.sub(r'@[A-Za-z0-9_]+', '', text)
    text = re.sub(r'https?://\S+|www\.\S+', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def clean_conversations() -> pd.DataFrame:
    if not CONVERSATIONS_CSV.exists():
        raise FileNotFoundError(f"Run build_conversations.py first. Missing {CONVERSATIONS_CSV}")
    
    df = pd.read_csv(CONVERSATIONS_CSV)
    df['clean_customer_text'] = df['customer_text'].apply(clean_tweet_text)
    df['clean_brand_text'] = df['brand_text'].apply(clean_tweet_text)
    
    initial_len = len(df)
    df = df[df['clean_customer_text'].str.len() >= 5].copy()
    
    df.to_csv(CLEANED_CONVERSATIONS_CSV, index=False)
    print(f"Cleaned dataset saved to: {CLEANED_CONVERSATIONS_CSV}")
    print(f"Removed {initial_len - len(df)} empty/short messages. Final count: {len(df):,}")
    return df

if __name__ == "__main__":
    clean_conversations()