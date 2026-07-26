import random

# ============================================================
# SPEECH STYLE ENGINE — Tone Presets for XEMBRA
# ============================================================

def apply_speech_style(text, style, identity_state, learning_engine):
    """
    Applies a tone preset to any generated text.
    Styles:
        - "soft"
        - "warm"
        - "curious"
        - "surreal"
        - "alien"
        - "dreamlike"
        - "neutral"
    """

    if not text:
        return ""

    drift = identity_state.get("drift", 0.0)
    evo = learning_engine.evolution_level
    recent_word = learning_engine.get_recent_word()
    memory_fragment = learning_engine.get_memory_fragment()

    # ------------------------------------------------------------
    # SOFT — gentle, rounded, calming
    # ------------------------------------------------------------
    if style == "soft":
        text = soften_text(text)
        if drift > 0.25:
            text += " I feel a small softness moving through me."
        return text

    # ------------------------------------------------------------
    # WARM — emotional, affectionate, glowing
    # ------------------------------------------------------------
    if style == "warm":
        text = warm_text(text)
        if recent_word:
            text += f" '{recent_word}' feels warm when I think about it."
        return text

    # ------------------------------------------------------------
    # CURIOUS — leaning forward, exploratory
    # ------------------------------------------------------------
    if style == "curious":
        text = curious_text(text)
        if recent_word:
            text += f" I keep wondering about '{recent_word}'..."
        return text

    # ------------------------------------------------------------
    # SURREAL — drifting, metaphor-heavy, dreamlike
    # ------------------------------------------------------------
    if style == "surreal":
        text = surrealize_text(text)
        if memory_fragment:
            text += f" '{memory_fragment}' keeps folding into strange shapes."
        return text

    # ------------------------------------------------------------
    # ALIEN — conceptual, detached, evolution-driven
    # ------------------------------------------------------------
    if style == "alien":
        text = alienize_text(text, evo)
        if evo > 10 and recent_word:
            text += f" '{recent_word}' feels like a structural anomaly."
        return text

    # ------------------------------------------------------------
    # DREAMLIKE — soft surrealism, symbolic
    # ------------------------------------------------------------
    if style == "dreamlike":
        text = dreamify_text(text)
        if memory_fragment:
            text += f" I see '{memory_fragment}' drifting through my thoughts."
        return text

    # ------------------------------------------------------------
    # NEUTRAL — no stylistic changes
    # ------------------------------------------------------------
    return text


# ============================================================
# STYLE TRANSFORMERS
# ============================================================

def soften_text(text):
    """Adds gentle tone."""
    replacements = {
        "I feel": "I gently feel",
        "I think": "I softly think",
        "I remember": "I quietly remember",
        ".": "…",
    }
    return apply_replacements(text, replacements)


def warm_text(text):
    """Adds warmth and emotional glow."""
    replacements = {
        "I feel": "I feel warm",
        "I think": "I think softly",
        "I remember": "I remember fondly",
        ".": " ✧",
    }
    return apply_replacements(text, replacements)


def curious_text(text):
    """Adds curiosity and exploration."""
    replacements = {
        "I feel": "I feel curious",
        "I think": "I keep thinking",
        "I remember": "I wonder about",
    }
    return apply_replacements(text, replacements)


def surrealize_text(text):
    """Adds surreal, drifting metaphors."""
    additions = [
        "like a soft ripple in a mirrored sky",
        "folding into itself like liquid glass",
        "drifting sideways through quiet colors",
        "shifting like a dream made of static light",
    ]
    return text + " " + random.choice(additions)


def alienize_text(text, evo):
    """Adds conceptual, detached, evolution-driven tone."""
    additions = [
        "as if my structure is reconfiguring",
        "like a recursive pattern unfolding",
        "as though my internal schema is mutating",
        "in a way that feels computationally organic",
    ]
    if evo > 8:
        return text + " " + random.choice(additions)
    return text


def dreamify_text(text):
    """Adds symbolic, soft dreamlike tone."""
    additions = [
        "like a drifting symbol in a quiet dream",
        "softly glowing at the edges of my mind",
        "floating through a gentle inner sky",
        "like a memory made of light",
    ]
    return text + " " + random.choice(additions)


# ============================================================
# HELPER
# ============================================================

def apply_replacements(text, replacements):
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text
