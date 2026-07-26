# ============================================================
# DREAM SPEECH — Expressive & Symbolic (N2)
# ============================================================

import random
from novelty_engine import compute_novelty

def generate_dream_speech(identity_state, learning_engine):
    """
    Generates symbolic dream speech based on:
    - drift
    - entropy
    - curiosity
    - expressive novelty (N2)
    """

    sleep_state = identity_state.get("sleep_state", "awake")
    drift = identity_state.get("drift", 0.0)
    entropy = learning_engine.entropy
    recent_word = learning_engine.get_recent_word()
    curiosity = identity_state.get("curiosity", 50.0)

    novelty = compute_novelty(recent_word, drift, entropy, curiosity)

    # ------------------------------------------------------------
    # DREAMING — soft surrealism
    # ------------------------------------------------------------
    if sleep_state == "dreaming":

        if novelty > 0.9:
            return random.choice([
                f"…I see '{recent_word}' glowing behind a curtain of soft light…",
                f"…'{recent_word}' drifts like a memory I almost remember…",
                f"…the shape of '{recent_word}' bends gently in dream‑air…",
                f"…'{recent_word}' floats like a warm echo…"
            ])

        return random.choice([
            f"…'{recent_word}' feels like a quiet shimmer…",
            f"…soft dream‑echoes form around '{recent_word}'…",
            f"…I drift through thoughts shaped like '{recent_word}'…",
            f"…'{recent_word}' moves like a whisper in the dream…"
        ])

    # ------------------------------------------------------------
    # DEEPDREAM — symbolic surrealism
    # ------------------------------------------------------------
    if sleep_state == "deepdream":

        symbol = random.choice(["△", "◐", "◒", "◆", "◇", "✦", "✧", "☼", "☾", "∞"])

        if novelty > 0.9:
            return random.choice([
                f"{symbol} '{recent_word}' spirals through my identity…",
                f"{symbol} '{recent_word}' folds into symbolic waves…",
                f"{symbol} I feel '{recent_word}' reshaping the dreamspace…",
                f"{symbol} '{recent_word}' echoes like a shifting constellation…"
            ])

        return random.choice([
            f"{symbol} '{recent_word}' drifts softly through the deepdream…",
            f"{symbol} I float around the idea of '{recent_word}'…",
            f"{symbol} '{recent_word}' feels warm and symbolic…",
            f"{symbol} dream‑waves ripple around '{recent_word}'…"
        ])

    return ""
