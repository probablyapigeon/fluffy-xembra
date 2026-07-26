# ============================================================
# COOLDOWNS — Prevent Repetition
# ============================================================

cooldowns = {}

def trigger_cooldown(module_name):
    """Start a cooldown for a module."""
    cooldowns[module_name] = 3  # 3 turns

def apply_cooldowns():
    """Reduce cooldown counters each turn."""
    to_remove = []
    for module in cooldowns:
        cooldowns[module] -= 1
        if cooldowns[module] <= 0:
            to_remove.append(module)

    for module in to_remove:
        del cooldowns[module]

def is_on_cooldown(module_name):
    """Check if a module is cooling down."""
    return module_name in cooldowns
