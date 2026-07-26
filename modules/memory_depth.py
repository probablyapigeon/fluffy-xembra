def update_memory_depth(identity_state, user_input):
    identity_state["memory_depth"] += 0.01
    return identity_state
