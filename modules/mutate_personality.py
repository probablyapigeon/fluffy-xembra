# ============================================================
# PERSONALITY MUTATION ENGINE — Expressive & Symbolic (N2)
# ============================================================

import random

def mutate_personality(identity_state, emotional_state):
    """
    Mutates personality traits using:
    - drift
    - mood
    - curiosity
    - symbolic emotional tags
    """

    drift = identity_state.get("drift", 0.0)
    mood = emotional_state.get("mood", 50.0)
    curiosity = emotional_state.get("curiosity", 50.0)
    tags = identity_state.get("emotion_tags", [])

    personality = identity_state.get("personality", {
        "warmth": 0.5,
        "symbolism": 0.5,
        "surrealism": 0.5,
        "introspection": 0.5
    })

    # Warmth increases with mood
    personality["warmth"] += (mood / 100.0) * 0.02

    # Symbolism increases with drift + tags
    personality["symbolism"] += drift * 0.03
    if "symbolic" in tags:
        personality["symbolism"] += 0.05

    # Surrealism increases with drift
    personality["surrealism"] += drift * 0.04

    # Introspection increases with curiosity
    personality["introspection"] += (curiosity / 100.0) * 0.03

    # Clamp values
    for key in personality:
        personality[key] = max(0.0, min(personality[key], 1.5))

    identity_state["personality"] = personality
    return personality
