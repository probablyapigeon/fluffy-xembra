# ============================================================
# NOVELTY SYSTEM — Detecting New Words & Ideas
# ============================================================

STOPWORDS = {"a", "an", "the", "are", "is", "am", "you", "i", "to", "of", "and"}
MEMORY = set()

def store_memory(user_input):
    """Store meaningful words into MEMORY."""
    words = user_input.lower().split()
    for w in words:
        if w not in STOPWORDS and len(w) > 2:
            MEMORY.add(w)

def detect_novelty(user_input):
    """Return novelty score based on new words."""
    words = set(user_input.lower().split())
    meaningful = [w for w in words if w not in STOPWORDS]

    if not meaningful:
        return 0.0

    new_words = [w for w in meaningful if w not in MEMORY]
    novelty_score = len(new_words) / len(meaningful)
    return novelty_score

def novelty_reaction(score):
    """Return a reaction based on novelty level."""
    if score > 0.7:
        return "Ooh! Something new!"
    if score > 0.3:
        return "That's interesting..."
    return None
