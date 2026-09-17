import os
from pathlib import Path

# Base Paths
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
OUTPUTS_DIR = BASE_DIR / "outputs"

# Ensure essential directories exist
DATA_DIR.mkdir(parents=True, exist_ok=True)
OUTPUTS_DIR.mkdir(parents=True, exist_ok=True)

# File Paths
RAW_CONVERSATIONS_JSON = DATA_DIR / "conversations.json"
CLEANED_CONVERSATIONS_CSV = DATA_DIR / "cleaned_conversations.csv"
INDEX_PATH = OUTPUTS_DIR / "faiss_index.bin"
METADATA_PATH = OUTPUTS_DIR / "metadata.pkl"

# Model & Vector Search Settings
MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
TOP_K = 3

# Taxonomy & Classification Settings
CONFIDENCE_THRESHOLD = 0.4