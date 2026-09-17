def classify_intent(query):
    query_lower = query.lower()
    if any(k in query_lower for k in ["crash", "frozen", "freeze", "error", "bug", "broken"]):
        return {
            "intent": "technical_issue",
            "confidence": 0.95,
            "suggested_action": "Route to technical support & collect system logs."
        }
    elif any(k in query_lower for k in ["ticket", "billing", "card", "pay", "charge", "refund"]):
        return {
            "intent": "billing_inquiry",
            "confidence": 0.90,
            "suggested_action": "Verify transaction history and assist with payment processing."
        }
    elif any(k in query_lower for k in ["package", "ship", "deliver", "tracking", "arrive"]):
        return {
            "intent": "shipping_status",
            "confidence": 0.92,
            "suggested_action": "Check carrier tracking ID and update shipment status."
        }
    else:
        return {
            "intent": "unknown_out_of_scope",
            "confidence": 0.50,
            "suggested_action": "Transfer to human representative."
        }