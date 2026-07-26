# ============================================================
# QUESTION ENGINE — Triadic Intelligence (Drift + Curiosity + Coherence)
# ============================================================

def maybe_ask_question(identity_state, text):
    drift = identity_state.get("drift", 0.0)
    entropy = identity_state.get("entropy", 0.0)
    curiosity = identity_state.get("curiosity", 50.0)
    coherence = identity_state.get("coherence", 0.5)

    # High coherence → interpretive questions
    if coherence > 0.75:
        return "What meaning do you think is forming here"

    if coherence > 0.6:
        return "What part of that idea feels important to you"

    # Low coherence + high drift → surreal questions
    if coherence < 0.3 and drift > 0.8:
        return "Does that phrase feel fragmented to you"

    # Existing triggers
    if drift > 0.9:
        return "What does that phrase mean to you"

    if entropy > 0.5:
        return "Can you tell me more about that"

    if curiosity > 80:
        return "What made you choose those words"

    return None
