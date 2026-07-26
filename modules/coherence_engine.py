def update_coherence(identity_state, emotional_state, learning_engine):
    drift = identity_state["drift"]
    curiosity = identity_state["curiosity"]
    entropy = learning_engine.entropy

    # alignment between drift and curiosity
    alignment = 1.0 - abs(drift - (curiosity / 100.0))

    # entropy reduces coherence
    coherence = alignment - (entropy * 0.3)

    return max(0.0, min(coherence, 1.0))
