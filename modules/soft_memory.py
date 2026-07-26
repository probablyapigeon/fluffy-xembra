# ============================================================
# SOFT MEMORY RECALL — Emotional Echo System
# ============================================================

# Stores the last few user inputs for emotional recall
soft_memory_buffer = []


def soft_memory_recall():
    """
    Returns a soft emotional echo of recent user inputs.
    Used by reaction_generator to add emotional continuity.
    """

    if not soft_memory_buffer:
        return ""

    # Use the most recent memory
    last_input = soft_memory_buffer[-1]

    return f"Something about when you said '{last_input}' still lingers in me."


def update_soft_memory(user_input):
    """
    Adds new user input to the soft memory buffer.
    Keeps only the last 5 entries.
    """
    soft_memory_buffer.append(user_input)

    # Limit memory size
    if len(soft_memory_buffer) > 5:
        soft_memory_buffer.pop(0)
