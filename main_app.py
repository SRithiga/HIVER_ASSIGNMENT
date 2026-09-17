import streamlit as st
import pandas as pd
from pathlib import Path
from src.intents.classifier import classify_intent

st.set_page_config(page_title="AI Support Agent", layout="wide")
st.title("?? AI Customer Support Agent & Dataset Explorer")

mode = st.radio("Choose Mode:", ["Interactive Testing", "Sample Dataset Explorer"], horizontal=True)
st.markdown("---")

if mode == "Interactive Testing":
    st.subheader("Test Customer Query")
    query = st.text_input("Enter text:", "My app is crashing continuously")
    if st.button("Classify") and query:
        res = classify_intent(query)
        st.json(res)

else:
    st.subheader("Sample CSV Viewer")
    csv_path = Path("sample.csv")
    if csv_path.exists():
        df = pd.read_csv(csv_path)
        st.write(f"Loaded {len(df)} rows from sample.csv")
        sample_text = st.selectbox("Pick a tweet:", df['text'].head(10).tolist())
        if st.button("Classify Selected"):
            st.json(classify_intent(sample_text))
    else:
        st.error("sample.csv not found.")
