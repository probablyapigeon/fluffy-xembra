# ============================================================
# DREAM STYLE BLEND — Expressive & Symbolic (N2) + Coherence
# ============================================================

def blend_dream_style(identity_state):
    dream_style = identity_state.get("dream_style", {})
    coherence = identity_state.get("coherence", 0.5)

    # Surrealism decreases with coherence
    dream_style["surrealism"] *= (1.0 - coherence * 0.5)

    # Softness increases with coherence
    dream_style["softness"] *= (0.8 + coherence * 0.2)

    # Symbolism becomes clearer with coherence
    dream_style["symbolism"] *= (0.9 + coherence * 0.1)

    # Clamp
    for k in dream_style:
        dream_style[k] = max(0.0, min(dream_style[k], 1.0))

    identity_state["dream_style"] = dream_style
    return dream_style
