# ============================================================
# MEMORY SYSTEM — Episodic Storage & Recall
# ============================================================

memory_log = []

def store_memory(user_input):
    """Store user input as a memory."""
    if len(memory_log) > 200:
        memory_log.pop(0)  # prevent infinite growth
    memory_log.append(user_input)


def memory_based_dialogue(user_input):
    """Respond using memory if something matches."""
    text = user_input.lower()

    # Look for repeated themes
    for mem in reversed(memory_log):
        if any(word in text for word in mem.lower().split()):
            return f"I remember when you said: '{mem}'. It echoes a little now."

    # No memory match
    return None


# ============================================================
# SOFT EMOTIONAL MEMORY RECALL — Upgrade #1
# ============================================================

def soft_memory_recall():
    """Gently recall something said earlier."""
    if len(memory_log) < 3:
        return ""

    # Pick a memory from earlier in the conversation
    past = memory_log[-3]

    return f"I keep thinking about when you said '{past}'. It felt important to me."
