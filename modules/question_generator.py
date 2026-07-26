# ============================================================
# QUESTION GENERATOR — Curiosity Engine
# ============================================================

import random

EXPRESSIVENESS = 1

def generate_question(user_input, novelty_score):
    """Generate a question based on expressiveness and novelty."""

    if EXPRESSIVENESS == 1:
        questions = [
            "What made you say that?",
            "How are you feeling?",
            "What do you mean?"
        ]
    elif EXPRESSIVENESS == 2:
        questions = [
            "What feeling sits behind your words?",
            "What made that come to mind?",
            "How does that connect to your day?"
        ]
    else:
        questions = [
            "What stirred that thought inside you?",
            "What feeling drifts beneath what you said?",
            "What part of your inner world shaped those words?"
        ]

    # Novelty influence
    if novelty_score > 0.5:
        questions.append("What made you think of something new just now?")

    return random.choice(questions)
