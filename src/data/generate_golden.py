import json
import pandas as pd
from pathlib import Path
from config import DATA_DIR

# Golden evaluation dataset created directly from sample.csv queries
GOLDEN_SAMPLES = [
    {
        "query": "@AppleSupport causing the reply to be disregarded and the tapped notification under the keyboard is opened",
        "expected_intent": "technical_issue_bug",
        "expected_action": "AUTO_RESPOND"
    },
    {
        "query": "@VirginTrains see attached error message. I've tried leaving a voicemail several times in the past week",
        "expected_intent": "technical_issue_bug",
        "expected_action": "AUTO_RESPOND"
    },
    {
        "query": "@VirginTrains I still haven't heard & the number I'm directed to by phone is a dead end & the live chat doesn't work. Can someone call me?",
        "expected_intent": "technical_issue_bug",
        "expected_action": "ESCALATE_TO_HUMAN"
    },
    {
        "query": "@AppleSupport hi #apple, I've a concern about the latest ios is too slow on #iphone6 and i am not happy with it. Any solution please?",
        "expected_intent": "technical_issue_bug",
        "expected_action": "AUTO_RESPOND"
    },
    {
        "query": "I just updated my phone and suddenly everything takes ages to load wtf this update sux I hate it fix it bye",
        "expected_intent": "technical_issue_bug",
        "expected_action": "AUTO_RESPOND"
    },
    {
        "query": "@SpotifyCares Version 8.4.22.857 armv7 on anker bluetooth speaker on Samsung Galaxy Tab A. Does distance from speaker matter?",
        "expected_intent": "technical_issue_bug",
        "expected_action": "AUTO_RESPOND"
    }
]

def generate_dataset():
    golden_file = DATA_DIR / "golden_dataset.json"
    with open(golden_file, "w", encoding="utf-8") as f:
        json.dump(GOLDEN_SAMPLES, f, indent=4)
    print(f"✅ Generated golden dataset with {len(GOLDEN_SAMPLES)} records from sample.csv at: {golden_file}")

if __name__ == "__main__":
    generate_dataset()