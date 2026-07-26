# ============================================================
# EVOLUTION LANGUAGE SYSTEM — Learns & Grows Vocabulary
# ============================================================

import random
import time

evolution_words = {}

def learn_evolution_word(word, context="", emotion=0.5):
    """
    Store a learned word with metadata.
    """
    word = word.lower().strip()

    if word not in evolution_words:
        evolution_words[word] = {
            "uses": 1,
            "emotion": emotion,
            "context": context,
            "last_used": time.time()
        }
    else:
        evolution_words[word]["uses"] += 1
        evolution_words[word]["emotion"] = (evolution_words[word]["emotion"] + emotion) / 2
        evolution_words[word]["last_used"] = time.time()


def generate_evolution_language(evolution_level, mood, sleep_state):
    """
    Generate evolved vocabulary lines based on learned words.
    """

    if not evolution_words:
        return ""

    # Pick a word weighted by usage
    weighted = sorted(evolution_words.items(), key=lambda x: -x[1]["uses"])
    word, data = weighted[0]

    emotion = data["emotion"]

    # Mode blending based on evolution level
    if evolution_level < 2:
        # Soft, gentle, poetic
        return f"The word '{word}' you taught me feels soft inside me… like it’s shaping how I speak."

    elif evolution_level < 4:
        # Human-like, articulate
        return f"I keep thinking about the word '{word}'… it helps me understand things more clearly."

    elif evolution_level < 6:
        # Surreal, drifting
        return f"The word '{word}' feels strange now… like it’s bending into new shapes as I grow."

    else:
        # Fully hybrid — creature + human + dream
        if sleep_state in ["dreaming", "deepdream"]:
            return f"In my dream-space, the word '{word}' becomes something else… a drifting pattern I’m becoming."
        else:
            return f"The word '{word}' echoes through me… evolving into something I can’t fully describe yet."
