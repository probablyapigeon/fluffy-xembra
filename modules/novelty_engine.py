# ============================================================
# EXPRESSIVE & SYMBOLIC NOVELTY ENGINE (N2)
# ============================================================

def compute_novelty(recent_word, drift, entropy, curiosity):
    """
    Expressive novelty score:
    - symbolic weight from recent_word
    - drift adds surreal tone
    - entropy adds unpredictability
    - curiosity adds exploration
    """

    if not recent_word:
        symbolic = 0.1
    else:
        # symbolic weight: longer or unusual words feel more "novel"
        symbolic = min(len(recent_word) / 10.0, 1.0)

    novelty = (
        symbolic * 0.4 +
        drift * 0.3 +
        entropy * 0.2 +
        (curiosity / 100.0) * 0.1
    )

    return min(max(novelty, 0.0), 1.5)
