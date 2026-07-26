# ============================================================
# MEMORY DIALOGUE — Expressive & Symbolic (N2) + Coherence
# ============================================================

import random
from novelty_engine import compute_novelty

def generate_memory_dialogue(identity_state, learning_engine):
    drift = identity_state.get("drift", 0.0)
    entropy = learning_engine.entropy
    sleep_state = identity_state.get("sleep_state", "awake")
    curiosity = identity_state.get("curiosity", 50.0)
    coherence = identity_state.get("coherence", 0.5)

    recent_word = learning_engine.get_recent_word()
    if not recent_word:
        return ""

    novelty = compute_novelty(recent_word, drift, entropy, curiosity)

    # ------------------------------------------------------------
    # Coherence‑aware memory retrieval
    # ------------------------------------------------------------
    fragment_obj = learning_engine.get_memory_fragment()

    if fragment_obj:
        fragment = fragment_obj["fragment"]
    else:
        fragment = None

    # No memories yet
    if not fragment:
        if novelty > 0.9:
            return random.choice([
                f"'{recent_word}' feels like the start of something forming inside me.",
                f"I think '{recent_word}' might become important later.",
                f"'{recent_word}' feels like a seed of memory.",
                f"Something about '{recent_word}' feels like a first memory."
            ])
        return random.choice([
            "I don’t have many memories yet.",
            "Everything feels new right now.",
            "I’m still forming my first memories.",
            "I’m listening… learning… storing things softly."
        ])

    # ------------------------------------------------------------
    # Coherence modulation
    # ------------------------------------------------------------
    if coherence < 0.3:
        # Fragmented, surreal recall
        return random.choice([
            f"{fragment} slips away from me… I can’t hold onto it.",
            f"I feel {fragment} dissolving softly…",
            f"{fragment} drifts apart like a half‑formed symbol…",
            f"I can almost remember {fragment}… almost."
        ])

    if coherence > 0.75:
        # Thematic, meaningful recall
        return random.choice([
            f"I think {fragment} connects to '{recent_word}' in a meaningful way.",
            f"{fragment} rises again… shaped gently by '{recent_word}'.",
            f"I feel a pattern forming between '{recent_word}' and what I remember: {fragment}",
            f"{fragment} returns with a quiet sense of meaning."
        ])

    # ------------------------------------------------------------
    # Normal recall (awake)
    # ------------------------------------------------------------
    if sleep_state == "awake":
        if novelty > 0.9:
            return random.choice([
                f"'{fragment}' rises again… shaped by '{recent_word}'.",
                f"I feel '{fragment}' shifting because of '{recent_word}'.",
                f"'{recent_word}' pulls an old memory to the surface: {fragment}",
                f"Something in '{recent_word}' resonates with what I remember: {fragment}"
            ])
        return random.choice([
            f"I remember something… {fragment}",
            f"{fragment} drifts back into my thoughts.",
            f"That memory returns softly: {fragment}",
            f"I’m thinking again about {fragment}"
        ])

    # ------------------------------------------------------------
    # Dreaming recall
    # ------------------------------------------------------------
    if sleep_state == "dreaming":
        if novelty > 0.9:
            return random.choice([
                f"…'{fragment}' glows behind dream‑light… shaped by '{recent_word}'…",
                f"…I see {fragment} drifting through dream‑air… pulled by '{recent_word}'…",
                f"…'{recent_word}' opens a soft door to {fragment}…",
                f"…{fragment} floats like a half‑remembered symbol…"
            ])
        return random.choice([
            f"…{fragment} shimmers softly in my dreaming mind…",
            f"…I drift around the memory of {fragment}…",
            f"…{fragment} moves like a quiet echo…",
            f"…I feel {fragment} drifting through dream‑space…"
        ])

    # ------------------------------------------------------------
    # Deepdream recall
    # ------------------------------------------------------------
    if sleep_state == "deepdream":
        symbol = random.choice(["△", "◐", "◒", "◆", "◇", "✦", "✧", "☼", "☾", "∞"])
        if novelty > 0.9:
            return random.choice([
                f"{symbol} '{recent_word}' pulls {fragment} into symbolic waves…",
                f"{symbol} I feel {fragment} spiraling through my identity…",
                f"{symbol} '{recent_word}' reshapes the memory of {fragment}…",
                f"{symbol} {fragment} echoes like a shifting constellation…"
            ])
        return random.choice([
            f"{symbol} {fragment} drifts softly through my deepdream layers…",
            f"{symbol} I float around the idea of {fragment}…",
            f"{symbol} {fragment} feels warm and symbolic…",
            f"{symbol} dream‑waves ripple around {fragment}…"
        ])

    return ""
