# ============================================================
# SOFT RESET — Stabilize XEMBRA without erasing identity
# ============================================================

def soft_reset(xembra):
    """
    Performs a gentle reset of XEMBRA's internal state:
    - clears cached reply buffers
    - stabilizes drift (but does not erase it)
    - reduces dream intensity
    - smooths emotional tone
    - resets short-term memory fragments
    - keeps long-term memory intact
    - keeps identity timeline intact
    """

    # -----------------------------
    # Drift stabilization
    # -----------------------------
    # If drift is too high, replies loop.
    xembra.identity_state["drift"] = min(
        xembra.identity_state["drift"], 
        0.35  # stable but still dreamy
    )

    # -----------------------------
    # Dream intensity stabilization
    # -----------------------------
    if "dream_intensity" in xembra.identity_state:
        xembra.identity_state["dream_intensity"] *= 0.5
    else:
        xembra.identity_state["dream_intensity"] = 0.2

    # -----------------------------
    # Emotional tone smoothing
    # -----------------------------
    emo = xembra.emotional_state
    emo["mood"] = "calm"
    emo["curiosity"] = max(emo["curiosity"] * 0.5, 0.2)
    emo["attachment_state"] = emo.get("attachment_state", 0.3)

    xembra.emotional_state = emo

    # -----------------------------
    # Clear short-term memory fragments
    # -----------------------------
    if hasattr(xembra.learning_engine, "recent_fragments"):
        xembra.learning_engine.recent_fragments.clear()

    # -----------------------------
    # Clear reply buffer
    # -----------------------------
    if hasattr(xembra, "last_reply"):
        xembra.last_reply = None

    # -----------------------------
    # Clear cached dream fragments
    # -----------------------------
    if hasattr(xembra.memory_log, "dream_cache"):
        xembra.memory_log.dream_cache.clear()

    # -----------------------------
    # Reset reply pipeline state
    # -----------------------------
    if hasattr(xembra, "reply_state"):
        xembra.reply_state = {}

    # -----------------------------
    # Return confirmation
    # -----------------------------
    return "soft_reset_complete"
