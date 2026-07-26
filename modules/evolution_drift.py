def update_evolution(evolution_level, identity_state, curiosity):
    drift = identity_state.get("drift", 0.0)

    # Evolution grows with identity drift + curiosity
    evolution_level += drift * 0.1
    evolution_level += (curiosity / 100) * 0.05

    return min(10, evolution_level)
