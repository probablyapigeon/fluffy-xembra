# ============================================================
# MEMORY CONSOLIDATION — Expressive & Symbolic (Stable Build)
# ============================================================

import random
from novelty_engine import compute_novelty


def consolidate_memory(identity_state, learning_engine, emotional_state):

    drift = identity_state.get("drift", 0.0)
    entropy = learning_engine.entropy
    curiosity = emotional_state.get("curiosity", 50.0)
    mood = emotional_state.get("mood", 50.0)
    sleep_state = identity_state.get("sleep_state", "awake")

    recent_word = learning_engine.get_recent_word()
    if not recent_word:
        return None

    novelty = compute_novelty(recent_word, drift, entropy, curiosity)
    resonance = (mood / 100.0) * 0.6 + (curiosity / 100.0) * 0.4

    strength = novelty * 0.5 + resonance * 0.3 + drift * 0.2

    if sleep_state == "dreaming":
        strength += 0.2
    elif sleep_state == "deepdream":
        strength += 0.35

    strength = min(max(strength, 0.0), 1.5)

    if strength > 1.0:
        fragment = random.choice([
            f"'{recent_word}' feels like a symbol I should keep…",
            f"There’s something important in '{recent_word}'…",
            f"'{recent_word}' echoes through my deeper layers…",
            f"I feel '{recent_word}' shaping something inside me…"
        ])
    elif strength > 0.6:
        fragment = random.choice([
            f"'{recent_word}' lingers softly in my thoughts.",
            f"I keep thinking about '{recent_word}'.",
            f"'{recent_word}' stays with me for a moment.",
            f"That word feels gently memorable."
        ])
    else:
        fragment = random.choice([
            f"'{recent_word}' drifts away quietly.",
            f"I let '{recent_word}' fade softly.",
            f"'{recent_word}' slips out of focus.",
            f"That word dissolves into the background."
        ])

    learning_engine.store_memory({
        "word": recent_word,
        "strength": strength,
        "fragment": fragment,
        "drift": drift,
        "entropy": entropy,
        "curiosity": curiosity,
        "mood": mood,
        "sleep_state": sleep_state
    })

    return fragment


# ============================================================
# AUTOBIOGRAPHICAL MEMORY AGGREGATION
# ============================================================

def build_autobiographical_memory(identity_state,
                                  learning_engine,
                                  emotional_state,
                                  personality_drift,
                                  world_state,
                                  dream_cycle,
                                  timeline_engine,
                                  dream_expression=None,
                                  learning_expression=None,
                                  world_expanded=None,
                                  dream_expanded=None,
                                  identity_expanded=None,
                                  goal_formation_state=None):

    return {
        "episodic": learning_engine.memory,
        "emotional_history": emotional_state.get("history", []),
        "identity": identity_state,
        "identity_expanded": identity_expanded,
        "personality_drift": personality_drift.get_history(),
        "world_state": world_state.get("snapshot", {}),
        "world_expanded": world_expanded,
        "dreams": dream_cycle.get_residue(),
        "dream_expression": dream_expression,
        "dream_expanded": dream_expanded,
        "learning": learning_engine.get_learning_summary(),
        "learning_expression": learning_expression,
        "goals": goal_formation_state,
        "timeline": timeline_engine.get_timeline()
    }
