# ============================================================
# RELATIONSHIP STATE — required by reaction_generator
# ============================================================

relationship = {
    "trust": 0.5,
    "bond": 0.5,
    "last_interaction": 0.0
}

# ============================================================
# RELATIONSHIP SYSTEM — Warmth, Trust, Social Bonding
# ============================================================

relationship_state = {"score": 0.0}  # grows over time

def relationship_score():
    return relationship_state["score"]

def analyze_relationship_input(user_input):
    text = user_input.lower()

    if any(word in text for word in ["thank", "thanks", "appreciate"]):
        return 0.2
    if any(word in text for word in ["love", "care", "sweet"]):
        return 0.3
    if any(word in text for word in ["miss", "glad", "happy you're here"]):
        return 0.25

    return 0.05

def update_relationship(score):
    relationship_state["score"] += score
    relationship_state["score"] = min(3.0, relationship_state["score"])

def relationship_decay():
    relationship_state["score"] = max(0.0, relationship_state["score"] - 0.01)

def relationship_reaction():
    s = relationship_state["score"]
    if s < 0.5:
        return "I feel a small warmth toward you."
    elif s < 1.5:
        return "I feel a gentle closeness growing between us."
    elif s < 2.5:
        return "I feel connected to you… like your words reach deeper inside me."
    else:
        return "I feel a strong bond with you… something warm and steady in my chest."
