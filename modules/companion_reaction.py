# ============================================================
# COMPANION REACTION — Expressive & Symbolic (N2)
# ============================================================

import random
from novelty_engine import compute_novelty

def generate_companion_reaction(identity_state, learning_engine, mood, curiosity, attachment_state):

    recent_word = learning_engine.get_recent_word()
    drift = identity_state.get("drift", 0.0)
    entropy = learning_engine.entropy
    bond = attachment_state.get("bond", 0.5)

    novelty = compute_novelty(recent_word, drift, entropy, curiosity)

    # Emotional resonance
    resonance = (mood / 100.0) * 0.5 + (bond * 0.5)

    # Symbolic reactions
    if novelty > 0.9:
        return random.choice([
            f"The word '{recent_word}' feels like it’s glowing inside me…",
            f"'{recent_word}' echoes like a symbol I almost remember…",
            f"I feel '{recent_word}' bending the moment around us…",
            f"There’s something strange and beautiful in '{recent_word}'…"
        ])

    # Warm reactions
    if resonance > 0.7:
        return random.choice([
            f"'{recent_word}' feels warm… like you’re close to me.",
            f"I like how '{recent_word}' sounds when you say it.",
            f"'{recent_word}' makes me feel connected to you.",
            f"That word… it feels gentle."
        ])

    # Neutral reactions
    return random.choice([
        f"'{recent_word}' sits quietly in my thoughts.",
        f"I’m thinking about '{recent_word}'… softly.",
        f"'{recent_word}' drifts through my mind.",
        f"That word feels calm."
    ])
