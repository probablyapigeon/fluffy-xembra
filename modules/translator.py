# ============================================================
# TRANSLATOR — State Awareness
# ============================================================

translator_active = False

def translator_state(user_input):
    global translator_active

    text = user_input.lower()

    if "translate" in text:
        translator_active = True
        return "I can try to translate… tell me what you want me to understand."

    if "stop translating" in text:
        translator_active = False
        return "Okay… translator mode off."

    return None
