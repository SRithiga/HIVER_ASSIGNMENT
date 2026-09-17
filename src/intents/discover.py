import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[2]))
from config import CLEANED_CONVERSATIONS_CSV, OUTPUTS_DIR

def discover_intents(n_clusters: int = 4):
    if not CLEANED_CONVERSATIONS_CSV.exists():
        raise FileNotFoundError(f"Missing input dataset: {CLEANED_CONVERSATIONS_CSV}")
    
    df = pd.read_csv(CLEANED_CONVERSATIONS_CSV)
    texts = df['clean_customer_text'].fillna('')
    
    vectorizer = TfidfVectorizer(max_features=500, stop_words='english')
    X = vectorizer.fit_transform(texts)
    
    n_clusters = min(n_clusters, len(df))
    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    df['cluster'] = kmeans.fit_predict(X)
    
    terms = vectorizer.get_feature_names_out()
    OUTPUTS_DIR.mkdir(parents=True, exist_ok=True)
    
    print("--- Discovered Intent Clusters ---")
    for i in range(n_clusters):
        center = kmeans.cluster_centers_[i]
        top_indices = center.argsort()[-5:][::-1]
        top_words = [terms[idx] for idx in top_indices if center[idx] > 0]
        print(f"Cluster {i}: Keywords -> {', '.join(top_words)}")
    
    output_path = OUTPUTS_DIR / "discovered_clusters.csv"
    df.to_csv(output_path, index=False)
    print(f"\nSaved clustered dataset to: {output_path}")

if __name__ == "__main__":
    discover_intents()