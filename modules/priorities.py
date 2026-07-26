# ============================================================
# PRIORITIES — Candidate Selection System
# ============================================================

def add_candidate(candidates, module_name, text):
    """
    Add a candidate reaction with a priority score.
    If text is None or empty, it is ignored.
    """
    if not text:
        return

    # Basic scoring: longer text = slightly higher priority
    score = len(text) * 0.01

    # Module-specific bias (you can tune these later)
    biases = {
        "emotion": 1.2,
        "relationship": 1.1,
        "attachment": 1.1,
        "identity": 1.0,
        "novelty": 0.9,
        "memory": 1.0,
        "reaction": 1.3,
        "question": 1.0,
        "scene": 0.8,
        "world_scene": 0.8,
        "goal": 0.7,
        "translator": 0.6,
        "thought": 0.5,
        "expressiveness": 0.3
    }

    score *= biases.get(module_name, 1.0)

    candidates.append((module_name, score, text))


# ============================================================
# SELECT BEST CANDIDATE
# ============================================================
def choose_best_candidate(candidates, mood):
    print("CHOOSE BEST CANDIDATE CALLED")
    if not candidates:
        return None

    # Sort by score (highest first)
    candidates.sort(key=lambda x: x[1], reverse=True)

    module_name, score, text = candidates[0]

    # ⭐ Speak the final chosen output ⭐
    speak(text, mood)

    return text
