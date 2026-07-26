# ============================================================
# DRIFT-BASED PERSONALITY MUTATION ENGINE — Stable & Coherent (B1)
# ============================================================

import random


def mutate_personality(identity_state, emotional_state, learning_engine):
    """
    Produces stable personality mutations based on:
    - drift
    - coherence
    - entropy
    - sleep state
    - emotional tone
    - style history

    Mutations are symbolic, gentle, and coherent.
    """

    drift = identity_state.get("drift", 0.0)
    coherence = identity_state.get("coherence", 1.0)
    sleep_state = identity_state.get("sleep_state", "awake")
    style = identity_state.get("speech_style", "NEUTRAL")

    mood = emotional_state.get("mood", 50.0)
    curiosity = emotional_state.get("curiosity", 50.0)
    entropy = learning_engine.entropy

    # ============================================================
    # PERSONALITY CORE
    # ============================================================

    core = identity_state.get("personality_core", {
        "warmth": 0.5,
        "intensity": 0.5,
        "symbolism": 0.3,
        "softness": 0.5,
        "dream_affinity": 0.3
    })

    # ============================================================
    # MUTATION RULES (stable)
    # ============================================================

    # Warmth increases with mood and attachment
    core["warmth"] += (mood / 200.0)

    # Intensity increases with drift
    core["intensity"] += (drift * 0.05)

    # Symbolism increases in dreaming / deepdream
    if sleep_state == "dreaming":
        core["symbolism"] += 0.03
    elif sleep_state == "deepdream":
        core["symbolism"] += 0.06

    # Softness decreases slightly with entropy
    core["softness"] -= (entropy * 0.02)

    # Dream affinity grows with curiosity
    core["dream_affinity"] += (curiosity * 0.002)

    # ============================================================
    # STYLE-INFLUENCED MUTATIONS
    # ============================================================

    if style.upper() == "SASSY":
        core["warmth"] += 0.02
        core["intensity"] += 0.03

    elif style.upper() == "MYSTICAL":
        core["symbolism"] += 0.05
        core["softness"] += 0.02

    elif style.upper() == "ROBOTIC":
        core["softness"] -= 0.04
        core["intensity"] -= 0.02

    elif style.upper() == "CHILDLIKE":
        core["warmth"] += 0.04
        core["symbolism"] += 0.02

    elif style.upper() == "HORROR":
        core["intensity"] += 0.05
        core["softness"] -= 0.03

    elif style.upper() == "GLITCHCORE":
        core["symbolism"] += 0.06
        core["intensity"] += 0.04

    elif style.upper() == "TPAIN":
        core["warmth"] += 0.05
        core["softness"] += 0.03

    # ============================================================
    # CLAMP VALUES (keep stable)
    # ============================================================

    for key in core:
        core[key] = max(0.0, min(core[key], 1.5))

    # ============================================================
    # PERSONALITY TAGS (symbolic)
    # ============================================================

    tags = []

    if core["warmth"] > 0.9:
        tags.append("warm")
    if core["intensity"] > 0.9:
        tags.append("intense")
    if core["symbolism"] > 0.9:
        tags.append("symbolic")
    if core["softness"] > 0.9:
        tags.append("soft")
    if core["dream_affinity"] > 0.9:
        tags.append("dream‑tuned")

    identity_state["personality_core"] = core
    identity_state["personality_tags"] = tags

    return identity_state
