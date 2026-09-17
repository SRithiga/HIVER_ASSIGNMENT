golden_path = DATA_DIR / "golden_dataset.json"
if not golden_path.exists():
    print("? golden_dataset.json not found! Run generate_golden.py first.")
    return

with open(golden_path, "r", encoding="utf-8") as f:
    samples = json.load(f)