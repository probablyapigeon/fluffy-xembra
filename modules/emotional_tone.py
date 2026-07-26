# ============================================================
# EMOTIONAL TONE ENGINE — Expressive & Symbolic (N2) + Coherence
# ============================================================

import random
from novelty_engine import compute_novelty

def update_emotional_tone(identity_state, emotional_state, learning_engine, *args):
    recent_word = learning_engine.get_recent_word()
    if not recent_word:
        return emotional_state

    drift = identity_state.get("drift", 0.0)
    entropy = learning_engine.entropy
    curiosity = emotional_state.get("curiosity", 50.0)
    mood = emotional_state.get("mood", 50.0)
    coherence = identity_state.get("coherence", 0.5)

    novelty = compute_novelty(recent_word, drift, entropy, curiosity)

    # Curiosity grows with novelty, but coherence focuses it
    curiosity += novelty * 4.0
    curiosity *= (0.6 + coherence * 0.4)

    # Mood shifts with drift + entropy, coherence stabilizes it
    mood += drift * 3.0
    mood += entropy * 2.0
    mood *= (0.7 + coherence * 0.3)

    # Clamp
    curiosity = max(0.0, min(curiosity, 100.0))
    mood = max(0.0, min(mood, 100.0))

    emotional_state["curiosity"] = curiosity
    emotional_state["mood"] = mood

    return emotional_state
