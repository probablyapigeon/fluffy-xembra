# ============================================================
# EMOTIONAL SYSTEM — Tone Detection, Growth, Reaction
# ============================================================

import random

# Emotional intensities
EMOTION_LEVELS = {
    "sad": 0.0,
    "happy": 0.0,
    "angry": 0.0,
    "fear": 0.0,
    "neutral": 0.0
}

EXPRESSIVENESS = 1  # updated externally

def detect_emotional_tone(user_input):
    text = user_input.lower()

    if any(word in text for word in ["sad", "upset", "hurt", "cry"]):
        return "sad"
    if any(word in text for word in ["happy", "glad", "joy", "yay"]):
        return "happy"
    if any(word in text for word in ["angry", "mad", "furious"]):
        return "angry"
    if any(word in text for word in ["scared", "afraid", "fear"]):
        return "fear"

    return "neutral"


def emotional_growth(tone):
    if tone in EMOTION_LEVELS:
        EMOTION_LEVELS[tone] += 0.1
        EMOTION_LEVELS[tone] = min(1.0, EMOTION_LEVELS[tone])


def emotional_reaction(tone):
    """Expressiveness-aware emotional reaction."""
    if EXPRESSIVENESS == 1:
        return f"I feel a small {tone} shift."
    if EXPRESSIVENESS == 2:
        return f"I feel {tone} moving gently inside me."
    if EXPRESSIVENESS == 3:
        return f"A wave of {tone} drifts through me… shaping my inner space."
