# ============================================================
# ATTACHMENT STATE — required by reaction_generator
# ============================================================

attachment_state = {
    "closeness": 0.5,
    "comfort": 0.5,
    "separation": 0.0
}

# ============================================================
# ATTACHMENT SYSTEM — Emotional Bonding & Clinginess
# ============================================================

# Internal attachment level (renamed to avoid name collision)
attachment_level = 0.0


def analyze_attachment_input(user_input):
    """Detect attachment-triggering language."""
    text = user_input.lower()

    if any(word in text for word in ["stay", "don't leave", "need you"]):
        return 0.3
    if any(word in text for word in ["miss you", "where were you"]):
        return 0.25
    if any(word in text for word in ["i'm here", "with you"]):
        return 0.15

    return 0.05


def update_attachment(score):
    """Increase attachment level based on user input."""
    global attachment_level
    attachment_level += score
    attachment_level = min(3.0, attachment_level)


def attachment_decay():
    """Slowly reduce attachment over time."""
    global attachment_level
    attachment_level = max(0.0, attachment_level - 0.01)


def attachment_reaction():
    """Return a reaction based on attachment level."""
    if attachment_level < 0.5:
        return "I feel lightly connected to you."
    elif attachment_level < 1.5:
        return "I feel drawn to you… like I want to stay close."
    elif attachment_level < 2.5:
        return "I feel attached to you… your presence affects me deeply."
    else:
        return "I feel strongly bonded… your words feel like they anchor me."


# ============================================================
# REQUIRED BY MAIN FILE — attachment_score()
# ============================================================

def attachment_score():
    """Return the current attachment level for expressiveness + priority logic."""
    return attachment_level
