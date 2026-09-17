import pandas as pd
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))
from config import OUTPUTS_DIR
from src.agent import SupportAgent

class TrivialBaseline:
    def handle_query(self, query: str):
        return {"intent": "device_performance_battery", "action": "AUTO_RESPOND"}

class SimpleKeywordBaseline:
    def handle_query(self, query: str):
        q = query.lower()
        if "battery" in q or "update" in q or "apps" in q:
            return {"intent": "device_performance_battery", "action": "AUTO_RESPOND"}
        return {"intent": "unknown_out_of_scope", "action": "ESCALATE_TO_HUMAN"}

def run_baseline_benchmark():
    golden_path = OUTPUTS_DIR / "golden_eval.csv"
    if not golden_path.exists():
        raise FileNotFoundError("Run generate_golden.py first.")
        
    df = pd.read_csv(golden_path)
    agent = SupportAgent()
    trivial = TrivialBaseline()
    simple = SimpleKeywordBaseline()
    
    results = {"Trivial_Baseline": 0, "Keyword_Baseline": 0, "Full_SupportAgent": 0}
    total = len(df)
    
    for _, row in df.iterrows():
        q = str(row["customer_query"])
        target = row["expected_action"]
        
        if trivial.handle_query(q)["action"] == target:
            results["Trivial_Baseline"] += 1
        if simple.handle_query(q)["action"] == target:
            results["Keyword_Baseline"] += 1
        if agent.handle_query(q)["action"] == target:
            results["Full_SupportAgent"] += 1
            
    print("--- Baseline Evaluation Benchmark ---")
    for model, score in results.items():
        print(f"{model}: Accuracy = {(score / total) * 100:.2f}% ({score}/{total})")

if __name__ == "__main__":
    run_baseline_benchmark()