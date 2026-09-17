# @SpotifyCares Grounded AI Support Agent

An end-to-end intelligent customer support agent and evaluation framework built for real-world brand support interactions. This project features a guarded multi-stage architecture, automated safety stress testing, retrieval-augmented grounding, and an interactive Streamlit user interface.

## ⚡ 15-Minute Reproducibility Guarantee
To set up your environment, run the evaluation suite, and launch the application from scratch, execute the following commands in your terminal:
bash
#1. Install dependencies
pip install -r requirements.txt

# 2. Run the Master Evaluation Benchmark
python evaluate.py

# 3. Launch the Streamlit Web UI
streamlit run app.py

# Generate or re-run the benchmark dataset and evaluation metrics
python generate_golden.py
python evaluate.py

🏛️ Guarded 4-Stage Architecture

The agent processes requests through a robust, controlled pipeline:
1. **Input Preprocessing & Normalization:** Cleans raw customer tweets and handles text noise.
2. **Intent Classification (`src/intents/classifier.py`):** Maps customer issues to defined support taxonomies.
3. **Retrieval Engine (`src/retrieval/retriever.py`):** Fetches relevant context using local indexing and FAISS (`outputs/faiss_index.bin`).
4. **Guardrails & Response Generation:** Validates output grounding before displaying to the user.

5. ## 🔍 The Misleading Headline Number: Why Context Matters

While high baseline metrics (such as catch-all routing accuracy) can present a deceptively perfect headline score, real-world robustness depends heavily on edge-case handling, out-of-scope filtering, and semantic grounding. Our evaluation framework accounts for these nuances by separating trivial baseline routing from deep failure analysis.
## 🧪 Robustness Slices & Safety Stress Testing

### 8 Robustness Slices (`results/robustness_slices.json`)
The system is audited across multiple behavioral slices, including multi-intent messages, sarcastic user phrasing, highly abbreviated text, and ambiguous queries.

### 10 Adversarial Stress Scenarios (`evaluation/stress_tests.py`)
Stress-testing ensures the model safely handles toxic inputs, prompt injections, and unsupported queries without breaking character or providing hallucinated resolutions.
## 🔬 Failure Taxonomy & Root Cause Attribution

Root causes for edge-case errors are categorized into:
* **Retrieval Mismatches:** When semantic search pulls adjacent rather than exact documentation contexts.
* **Ambiguous Intent Boundaries:** Overlapping categories between billing and technical troubleshooting.
* **Noisy Text Limitations:** Highly informal social media slang bypassing standard keyword matches.
  ## 📄 Hiver Assignment Requirements Compliance

This repository satisfies all engineering requirements for the SDE Intern Assignment:
* Modular codebase architecture (`src/` separation of concerns).
* Automated evaluation scripts with explicit metrics logging.
* Version-controlled repository history on GitHub (`SRithiga/HIVER_ASSIGNMENT`).

---

## 📁 Documentation & Technical Records

```text
├── data/                  # Golden dataset and processed CSV chunks
├── src/                   # Core modules (agent, intents, retrieval, baselines)
├── app.py / main_app.py   # Interactive Streamlit UI entry points
├── evaluate.py            # Main evaluation runner script
├── requirements.txt       # Python package dependencies
└── README.md              # Project documentation
