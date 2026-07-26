import random

def update_curiosity(curiosity, novelty_score):
    # Novelty increases curiosity
    curiosity += novelty_score * 0.1

    # Natural drift
    curiosity += random.uniform(-2, 2)

    curiosity = max(0, min(100, curiosity))
    return curiosity
