import random

def update_attachment(attachment_state, user_input):
    closeness = attachment_state.get("closeness", 0.5)
    comfort = attachment_state.get("comfort", 0.5)
    separation = attachment_state.get("separation", 0.0)

    # Positive words increase closeness
    if any(word in user_input.lower() for word in ["hi", "hello", "welcome", "thank", "love"]):
        closeness += 0.05
        comfort += 0.03

    # Negative words increase separation
    if any(word in user_input.lower() for word in ["leave", "stop", "hate", "go away"]):
        separation += 0.1
        closeness -= 0.05

    # Natural drift
    closeness += random.uniform(-0.01, 0.01)
    comfort += random.uniform(-0.01, 0.01)

    closeness = max(0.0, min(1.0, closeness))
    comfort = max(0.0, min(1.0, comfort))
    separation = max(0.0, min(1.0, separation))

    attachment_state["closeness"] = closeness
    attachment_state["comfort"] = comfort
    attachment_state["separation"] = separation

    return attachment_state
