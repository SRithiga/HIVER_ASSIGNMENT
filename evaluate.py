import json
from pathlib import Path
from config import DATA_DIR
from src.agent import SupportAgent

def run_evaluation():
    golden_path = DATA_DIR / "golden_dataset.json"
    if not golden_path.exists():
        print("? golden_dataset.json not found! Run generate_golden.py first.")
        return

    with open(golden_path, "r", encoding="utf-8") as f:
        samples = json.load(f)

    agent = SupportAgent()
    correct_intents = 0
    total = len(samples)

    print("\n--- Running Evaluation Benchmark ---")
    for idx, item in enumerate(samples, 1):
        query = item["query"]
        expected_intent = item["expected_intent"]
        
        # Run through classification/agent
        result = agent.process_query(query) if hasattr(agent, 'process_query') else {}
        predicted_intent = result.get("intent", "unknown_out_of_scope")
        
        is_correct = predicted_intent == expected_intent
        if is_correct:
            correct_intents += 1

        print(f"\n[{idx}/{total}] Query: {query}")
        print(f" Expected: {expected_intent} | Predicted: {predicted_intent} | Match: {'?' if is_correct else '?'}")

    accuracy = (correct_intents / total) * 100 if total > 0 else 0
    print(f"\n====================================")
    print(f" Overall Intent Accuracy: {accuracy:.2f}% ({correct_intents}/{total})")
    print(f"====================================\n")

if __name__ == "__main__":
    run_evaluation()
