import streamlit as st
import pandas as pd
from pathlib import Path

st.title("🏷️ Golden Set Labeling Interface")

candidates_path = Path("golden_candidates.csv")
if candidates_path.exists():
    df = pd.read_csv(candidates_path)
    
    # Use Streamlit's data editor for interactive labeling
    edited_df = st.data_editor(df, num_rows="dynamic", use_container_width=True)
    
    if st.button("Save Golden Evaluation Set"):
        edited_df.to_csv("golden_eval.csv", index=False)
        st.success("Successfully saved as `golden_eval.csv`!")
else:
    st.warning("Please run `src/data/generate_golden.py` first to generate the candidate CSV.")



