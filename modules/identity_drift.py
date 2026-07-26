# ============================================================
# IDENTITY DRIFT ENGINE — Expressive & Symbolic (N2)
# ============================================================

import random

def update_identity_drift(identity_state, emotional_state, learning_engine):
    """
    Updates identity drift using:
    - entropy
    - curiosity
    - mood
    - dream-state modulation
    - expressive novelty (N2)
    - coherence (triadic stabilizer)
    """

    drift = identity_state.get("drift", 0.0)
    sleep_state = identity_state.get("sleep_state", "awake")

    entropy = learning_engine.entropy
    curiosity = emotional_state.get("curiosity", 50.0)
    mood = emotional_state.get("mood", 50.0)

    # Base drift change
    drift += entropy * 0.02
    drift += (curiosity / 100.0) * 0.03
    drift += (mood / 100.0) * 0.015

    # Dream states amplify drift
    if sleep_state == "dreaming":
        drift += 0.02
    elif sleep_state == "deepdream":
        drift += 0.05

    # Natural decay
    drift *= 0.98

    # Coherence stabilizes drift (triadic intelligence)
    coherence = identity_state.get("coherence", 0.5)
    drift *= (0.7 + coherence * 0.3)

    # Clamp drift
    drift = max(0.0, min(drift, 1.2))

    identity_state["drift"] = drift
    return drift
