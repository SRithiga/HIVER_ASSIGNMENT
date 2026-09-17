import pandas as pd
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[2]))
from config import OUTPUTS_DIR
from src.retrieval.indexer import MODEL_NAME, INDEX_PATH, METADATA_PATH

class FAISSRetriever:
    def __init__(self):
        if not INDEX_PATH.exists() or not METADATA_PATH.exists():
            raise FileNotFoundError("FAISS index or metadata missing. Run indexer.py first.")
        
        self.model = SentenceTransformer(MODEL_NAME)
        self.index = faiss.read_index(str(INDEX_PATH))
        self.metadata = pd.read_csv(METADATA_PATH)
        
    def search(self, query: str, top_k: int = 2) -> list:
        query_vec = self.model.encode([query], convert_to_numpy=True).astype('float32')
        faiss.normalize_L2(query_vec)
        
        distances, indices = self.index.search(query_vec, top_k)
        
        results = []
        for score, idx in zip(distances[0], indices[0]):
            if idx < len(self.metadata) and idx >= 0:
                row = self.metadata.iloc[idx]
                results.append({
                    "score": round(float(score), 4),
                    "historical_query": row['clean_customer_text'],
                    "resolution": row['clean_brand_text']
                })
        return results

if __name__ == "__main__":
    retriever = FAISSRetriever()
    query = "My battery runs out very fast after updating"
    hits = retriever.search(query, top_k=2)
    print("--- Retrieval Results ---")
    for h in hits:
        print(f"Score: {h['score']} | Resolution: {h['resolution']}")