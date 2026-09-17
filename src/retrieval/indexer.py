import pandas as pd
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[2]))
from config import CLEANED_CONVERSATIONS_CSV, OUTPUTS_DIR

MODEL_NAME = 'all-MiniLM-L6-v2'
INDEX_PATH = OUTPUTS_DIR / "faiss_index.bin"
METADATA_PATH = OUTPUTS_DIR / "retrieval_metadata.csv"

def build_index():
    if not CLEANED_CONVERSATIONS_CSV.exists():
        raise FileNotFoundError(f"Missing cleaned dataset at {CLEANED_CONVERSATIONS_CSV}")
    
    df = pd.read_csv(CLEANED_CONVERSATIONS_CSV)
    texts = df['clean_customer_text'].fillna('').tolist()
    
    print(f"Loading embedding model: {MODEL_NAME}...")
    model = SentenceTransformer(MODEL_NAME)
    
    print("Generating embeddings for historical queries...")
    embeddings = model.encode(texts, show_progress_bar=True, convert_to_numpy=True)
    embeddings = embeddings.astype('float32')
    
    # Normalize embeddings for cosine similarity using Inner Product
    faiss.normalize_L2(embeddings)
    
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatIP(dimension)
    index.add(embeddings)
    
    OUTPUTS_DIR.mkdir(parents=True, exist_ok=True)
    faiss.write_index(index, str(INDEX_PATH))
    df.to_csv(METADATA_PATH, index=False)
    
    print(f"FAISS index built successfully with {index.ntotal} vectors.")
    print(f"Saved index to: {INDEX_PATH}")

if __name__ == "__main__":
    build_index()