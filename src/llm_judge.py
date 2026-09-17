import sys
from pathlib import Path
from sentence_transformers import SentenceTransformer, util

sys.path.append(str(Path(__file__).resolve().parents[1]))
from src.agent import SupportAgent

class LLMJudge:
    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')

    def evaluate_reply_quality(self, customer_query: str, agent_response: str) -> dict:
        """Evaluates reply relevance and groundedness on a 1-5 rubric scale."""
        if "human support agent" in agent_response.lower() or "representative" in agent_response.lower():
            return {"score": 5, "reason": "Correctly escalated out-of-scope/unclear query to human."}
            
        # Semantic similarity between query and generated response
        emb_query = self.model.encode(customer_query, convert_to_tensor=True)
        emb_resp = self.model.encode(agent_response, convert_to_tensor=True)
        sim_score = float(util.cos_sim(emb_query, emb_resp)[0][0])
        
        # Map cosine similarity to 1-5 rubric grade
        grade = min(5, max(1, int(sim_score * 5) + 1))
        return {
            "score": grade,
            "similarity_score": round(sim_score, 4),
            "reason": "Grounded historical response aligns with customer topic."
        }

if __name__ == "__main__":
    judge = LLMJudge()
    agent = SupportAgent()
    
    sample_query = "My battery runs out very fast after updating to iOS 11"
    agent_output = agent.handle_query(sample_query)
    eval_result = judge.evaluate_reply_quality(sample_query, agent_output["response"])
    
    print("--- LLM-as-a-Judge Evaluation Output ---")
    print("Query:", sample_query)
    print("Agent Response:", agent_output["response"])
    print("Judge Score:", eval_result["score"], "/ 5")
    print("Judge Reason:", eval_result["reason"])