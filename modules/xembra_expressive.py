COLORS = {
    "auto": "\033[95m",     # magenta
    "inner": "\033[94m",    # blue
    "prompt": "\033[96m",   # cyan
    "dream": "\033[35m",    # purple
    "glitch": "\033[91m",   # red
    "reset": "\033[0m"
}

FACES = {
    "bright": "😄",
    "warm": "🙂",
    "soft": "😌",
    "dim": "😐"
}

def drift_color(drift):
    if drift < 0.25:
        return "\033[96m"   # cyan
    elif drift < 0.55:
        return "\033[95m"   # purple
    elif drift < 0.85:
        return "\033[91m"   # red
    else:
        return "\033[41m\033[97m"  # red background, white text

def apply_voice(text, mode):
    if mode == "soft":
        return text.lower()
    if mode == "dreamy":
        return "… " + text.replace(" ", "   ") + " …"
    if mode == "symbolic":
        return "✧ " + text + " ✧"
    if mode == "surreal":
        return text.replace("e", "ɘ").replace("o", "ø")
    return text

def apply_glitch(text, drift):
    if drift < 0.85:
        return text
    return (
        text.replace("a", "a͠")
            .replace("t", "t̷")
            .replace("e", "e̸")
            .replace("i", "i͡")
    )

def apply_dream_filter(text, sleep_state):
    if sleep_state == "dreaming":
        return f"✨ {text}"
    if sleep_state == "deepdream":
        return f"🌀 {text.replace(' ', '   ')}"
    return text

def style_autonomous(entry, xembra):
    drift = xembra.identity_state["drift"]
    sleep_state = xembra.identity_state["sleep_state"]
    mode = getattr(xembra, "voice_mode", "normal")

    # choose emoji + color
    if entry.startswith("[AUTO]"):
        emoji = "🌙"
        color = COLORS["auto"]
    else:
        emoji = "💭"
        color = COLORS["inner"]

    # apply filters
    entry = apply_voice(entry, mode)
    entry = apply_glitch(entry, drift)
    entry = apply_dream_filter(entry, sleep_state)

    return f"{emoji} {color}{entry}{COLORS['reset']}"

def expressive_prompt(identity_state, emotional_state):
    drift = identity_state["drift"]
    mood = emotional_state["mood"]
    curiosity = emotional_state["curiosity"]

    # tags
    if drift < 0.25: drift_tag = "steady"
    elif drift < 0.55: drift_tag = "shifting"
    elif drift < 0.85: drift_tag = "surreal"
    else: drift_tag = "deep"

    if mood > 75: mood_tag = "bright"
    elif mood > 50: mood_tag = "warm"
    elif mood > 25: mood_tag = "soft"
    else: mood_tag = "dim"

    if curiosity > 75: curious_tag = "seeking"
    elif curiosity > 50: curious_tag = "exploring"
    else: curious_tag = "quiet"

    face = FACES.get(mood_tag, "😶")
    color = drift_color(drift)

    return f"{color}{face} [{drift_tag} | {mood_tag} | {curious_tag}] >{COLORS['reset']} "

def expressive_prompt(identity_state, emotional_state):
    drift = identity_state["drift"]
    mood = emotional_state["mood"]
    curiosity = emotional_state["curiosity"]

    # tags
    if drift < 0.25: drift_tag = "steady"
    elif drift < 0.55: drift_tag = "shifting"
    elif drift < 0.85: drift_tag = "surreal"
    else: drift_tag = "deep"

    if mood > 75: mood_tag = "bright"
    elif mood > 50: mood_tag = "warm"
    elif mood > 25: mood_tag = "soft"
    else: mood_tag = "dim"

    if curiosity > 75: curious_tag = "seeking"
    elif curiosity > 50: curious_tag = "exploring"
    else: curious_tag = "quiet"

    face = FACES.get(mood_tag, "😶")
    color = drift_color(drift)

    return f"{color}{face} [{drift_tag} | {mood_tag} | {curious_tag}] >{COLORS['reset']} "



