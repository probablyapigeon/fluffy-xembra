# ============================================================
# WORLD SCENE — Seasons, Weather, Mood
# ============================================================

import random

world_state = {
    "season": "spring",
    "weather": "clear",
    "mood": "calm"
}

def update_season():
    """Cycle through seasons slowly."""
    order = ["spring", "summer", "autumn", "winter"]
    current = world_state["season"]
    next_index = (order.index(current) + 1) % len(order)
    world_state["season"] = order[next_index]


def update_weather():
    """Random weather shifts."""
    options = ["clear", "cloudy", "rainy", "stormy", "foggy"]
    world_state["weather"] = random.choice(options)


def update_world_mood_expressiveness(expressiveness):
    """Mood influenced by expressiveness."""
    if expressiveness == 1:
        world_state["mood"] = "calm"
    elif expressiveness == 2:
        world_state["mood"] = "warm"
    else:
        world_state["mood"] = "vivid"


def render_world_scene():
    """Return a description of her inner world."""
    season = world_state["season"]
    weather = world_state["weather"]
    mood = world_state["mood"]

    return (
        f"Inside me, it feels like {season}. "
        f"The weather is {weather}, and the mood feels {mood}."
    )
