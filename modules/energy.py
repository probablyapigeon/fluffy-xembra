import random

def drain_energy(energy, mood):
    """
    Energy drains slightly each turn.
    Mood affects drain rate.
    """
    # baseline drain
    drain = random.uniform(4, 8)

    # mood affects drain
    if mood < 30:
        drain += 1.5
    elif mood > 70:
        drain -= 0.5

    energy -= drain
    return max(0, min(100, energy))


def regen_energy(energy):
    """
    Regenerate energy slowly if above certain thresholds.
    """
    if energy < 30:
        energy += random.uniform(0.5, 1.5)
    elif energy > 70:
        energy += random.uniform(0.1, 0.3)

    return max(0, min(100, energy))
