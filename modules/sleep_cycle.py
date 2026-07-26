import random

def update_sleep_state(sleep_state, energy):
    """
    Basic sleep/tired/rested states.
    """
    if energy < 20:
        return "tired"
    elif energy > 80:
        return "rested"
    return sleep_state


def maybe_enter_dream_state(sleep_state, energy, identity_state):
    """
    Enter dreaming or deepdream based on:
    - low energy
    - identity drift
    - memory depth
    """
    drift = identity_state.get("drift", 0.0)
    memory_depth = identity_state.get("memory_depth", 0.0)

    # Enter dreaming
    if sleep_state == "tired" and energy < 40:
        if random.random() < 0.4 + drift * 0.2:
            return "dreaming"

    # Enter deepdream
    if sleep_state == "dreaming":
        if memory_depth > 0.2 or drift > 0.3:
            if random.random() < 0.3 + memory_depth * 0.3:
                return "deepdream"

    # Wake from dream states
    if sleep_state in ["dreaming", "deepdream"] and energy > 40:
        if random.random() < 0.3:
            return "awake"

    return sleep_state
