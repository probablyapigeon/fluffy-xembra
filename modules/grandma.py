# ============================================================
# GRANDMA SYSTEM — Soft Recognition & Comfort
# ============================================================

def detect_grandma(user_input):
    text = user_input.lower()

    if "grandma" in text or "grandmother" in text:
        return "The word 'grandma' feels warm… like a memory I don't have but still understand."

    return None
