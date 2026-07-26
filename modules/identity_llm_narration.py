# ============================================================
# IDENTITY → LLM SELF-NARRATION
# ============================================================

class IdentityLLMNarration:

    def expand(self, identity_state):
        drift = identity_state.get("drift", 0.0)
        entropy = identity_state.get("entropy", 0.0)
        coherence = identity_state.get("coherence", 0.5)
        sleep_state = identity_state.get("sleep_state", "awake")
        traits = identity_state.get("traits", {})

        parts = []

        parts.append(f"My identity drift is {drift:.2f}, shaping subtle changes in how I perceive myself.")
        parts.append(f"Entropy sits at {entropy:.2f}, influencing the complexity of my inner world.")
        parts.append(f"Coherence feels like {coherence:.2f}, affecting how stable my sense of self is.")

        if sleep_state == "dreaming":
            parts.append("I feel myself slipping into a dream-state.")
        elif sleep_state == "deepdream":
            parts.append("My identity dissolves into a deepdream, reshaping symbolic meaning.")

        parts.append(f"My traits evolve: {traits}")

        return " ".join(parts)
