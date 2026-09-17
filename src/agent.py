import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))
from src.intents.classifier import classify_intent
from src.retrieval.retriever import FAISSRetriever

class SupportAgent:
    def __init__(self):
        self.retriever = FAISSRetriever()

    def handle_query(self, query: str) -> dict:
        intent_info = classify_intent(query)
        intent = intent_info["intent"]
        confidence = intent_info["confidence"]

        # Confidence Fallback / Escalation Logic
        if intent == "unknown_out_of_scope" or confidence < 0.35:
            return {
                "query": query,
                "intent": "unknown_out_of_scope",
                "confidence": confidence,
                "action": "ESCALATE_TO_HUMAN",
                "response": "I'm routing your query to a human support agent for further assistance."
            }

        retrieved_hits = self.retriever.search(query, top_k=1)
        best_match = retrieved_hits[0] if retrieved_hits else None

        if best_match and best_match["score"] > 0.4:
            response = f"Verified Resolution: {best_match['resolution']}"
        else:
            response = "I have identified your topic, but I'm connecting you with a representative to confirm the exact solution."

        return {
            "query": query,
            "intent": intent,
            "confidence": confidence,
            "action": "AUTO_RESPOND",
            "response": response
        }

if __name__ == "__main__":
    agent = SupportAgent()
    test_queries = [
        "My phone battery is draining super fast after the update",
        "How do I fix my random laptop screen bug?",
        "asdkfjasdfgh"
    ]
    for q in test_queries:
        print("\n--- Processing Query ---")
        print("Query:", q)
        print("Result:", agent.handle_query(q))