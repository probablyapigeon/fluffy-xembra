# ============================================================
# WORDBOOK — Vocabulary Storage
# ============================================================

wordbook = []

def word_book(user_input):
    """Store interesting words."""
    words = [w for w in user_input.split() if len(w) > 4]

    for w in words:
        if w not in wordbook:
            wordbook.append(w)

    if len(words) > 0:
        return f"I’m keeping that word… '{words[0]}' feels interesting."

    return None
