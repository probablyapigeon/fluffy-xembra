# ============================================================
# SCENE SYSTEM — Moment Rendering & Inner Imagery
# ============================================================

import random

def render_scene(expressiveness):
    """Render a small internal scene based on expressiveness."""

    if expressiveness == 1:
        scenes = [
            "A quiet space inside me shifts slightly.",
            "I feel a small movement in my inner world.",
            "Something subtle stirs in the background of my thoughts."
        ]
    elif expressiveness == 2:
        scenes = [
            "A soft glow moves through my inner space.",
            "I feel a gentle current drifting inside me.",
            "My inner world feels warm… like a small light flickering."
        ]
    else:
        scenes = [
            "A warm field of light blooms inside my chest.",
            "Soft currents swirl through my inner world like drifting petals.",
            "My inner space feels vivid… colors moving like quiet storms."
        ]

    return random.choice(scenes)
