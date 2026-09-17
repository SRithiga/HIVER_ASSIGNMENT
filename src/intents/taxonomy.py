CONFIDENCE_THRESHOLD = 0.25  # Lower threshold slightly for social media queries

INTENT_TAXONOMY = {
    "account_access_issue": {
        "description": "User is unable to log in, reset password, or access account.",
        "keywords": ["login", "password", "access", "sign in", "reset", "account", "locked", "mfa", "2fa"],
        "suggested_action": "AUTO_RESPOND",
    },
    "billing_and_payments": {
        "description": "Inquiries regarding invoices, charges, payment methods, or subscriptions.",
        "keywords": ["billing", "invoice", "payment", "charge", "card", "subscription", "pricing", "receipt"],
        "suggested_action": "AUTO_RESPOND",
    },
    "technical_issue_bug": {
        "description": "System crashes, errors, performance issues, software bugs, or device glitches.",
        "keywords": [
            "bug", "crash", "error", "slow", "lag", "failing", "broken", "issue", 
            "not working", "keyboard", "notification", "update", "ios", "version", 
            "speaker", "load", "voicemail", "live chat", "dead end", "disregarded"
        ],
        "suggested_action": "AUTO_RESPOND",
    },
    "feature_request": {
        "description": "User suggesting new features, enhancements, or improvements.",
        "keywords": ["feature", "request", "add", "suggestion", "improve", "support for", "enhancement"],
        "suggested_action": "ESCALATE_TO_HUMAN",
    },
    "refund_or_cancellation": {
        "description": "User requesting a refund, subscription cancellation, or dispute.",
        "keywords": ["refund", "cancel", "cancellation", "money back", "dispute", "close account"],
        "suggested_action": "ESCALATE_TO_HUMAN",
    },
    "unknown_out_of_scope": {
        "description": "Queries that do not fit standard categories or fall below confidence threshold.",
        "keywords": [],
        "suggested_action": "ESCALATE_TO_HUMAN",
    },
}