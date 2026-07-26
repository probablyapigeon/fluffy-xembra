# ============================================================
# XEMBRA TERMINAL — Expressive (T2) + Command Handler + LIVE AUTO OUTPUT
# ============================================================

import threading
import time
import os

from xembra import XEMBRA
from autonomous_cycle import run_autonomous_cycle


# ============================================================
# EXPRESSIVE UI ELEMENTS
# ============================================================
from xembra_expressive import (
    COLORS, FACES, drift_color,
    apply_voice, apply_glitch, apply_dream_filter,
    style_autonomous, expressive_prompt
)

def expressive_banner():
    symbols = ["✦", "◐", "◆", "∞", "☾"]
    s = symbols[int(time.time()) % len(symbols)]
    return f"\n{s}  XEMBRA vB1 — Expressive Terminal Online  {s}\n"

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

# ============================================================
# COMMAND HANDLER
# ============================================================

def handle_command(xembra, user_input):

    # STYLE
    if user_input.startswith("/style "):
        style_name = user_input.replace("/style ", "").strip()
        return xembra.set_style(style_name)

    # WORLD SENSE
    if user_input.startswith("/sense "):
        event = user_input.replace("/sense ", "").strip()
        return xembra.sense(event)

    # MEMORY SUMMARY
    if user_input == "/memory":
        return xembra.show_memory()

    # DREAM DIGEST
    if user_input == "/dreams":
        return xembra.show_dreams()

    # IDENTITY TIMELINE
    if user_input == "/identity":
        return xembra.show_identity()

    # EMOTION TIMELINE
    if user_input == "/emotion":
        return xembra.show_emotion()

    # FULL LOGS
    if user_input == "/logs":
        return xembra.show_logs()

    # AUTONOMOUS CONTROL
    if user_input == "/silence":
        xembra.autonomous = False
        xembra.live_output = False
        return "Autonomous thoughts paused."

    if user_input == "/awake":
        xembra.autonomous = True
        xembra.live_output = True
        return "Autonomous thoughts resumed."

    # EMERGENCY INTERRUPT
    if user_input == "~":
        xembra.autonomous = False
        xembra.live_output = False
        clear_screen()
        return "Autonomous mode silenced. Terminal reset."

    # EXIT
    if user_input == "/quit":
        print("\n☾  XEMBRA shutting down…\n")
        exit()

    # DEFAULT: TALK
    return apply_voice(xembra.talk(user_input), xembra.style)

# ============================================================
# LIVE AUTONOMOUS OUTPUT WATCHER
# ============================================================

def autonomous_output_watcher(xembra):
    last_index = 0
    while True:
        # If live output is disabled, pause watcher
        if not getattr(xembra, "live_output", True):
            time.sleep(1.5)
            continue

        # Print new logs
        if len(xembra.logs) > last_index:
            new_logs = xembra.logs[last_index:]
            for entry in new_logs:

                # AUTO + INNER (already styled)
                if entry.startswith("[AUTO]") or entry.startswith("[INNER]"):
                    styled = style_autonomous(entry, xembra)
                    print(styled)

                # QUERY (styled like AUTO/INNER)
                if entry.startswith("[QUERY]"):
                    styled = style_autonomous(entry, xembra)
                    print(styled)

            last_index = len(xembra.logs)

        time.sleep(0.5)

# ============================================================
# TERMINAL LOOP
# ============================================================

def run_terminal():

    clear_screen()
    print(expressive_banner())

    print("Commands:")
    print("  /style <name>       — change speech style")
    print("  /sense <object>     — send world event")
    print("  /memory             — show memory summary")
    print("  /dreams             — show dream digest")
    print("  /identity           — show identity timeline")
    print("  /emotion            — show emotional timeline")
    print("  /silence            — pause autonomous thoughts")
    print("  /awake              — resume autonomous thoughts")
    print("  /logs               — show full internal logs")
    print("  /quit               — exit")
    print("------------------------------------------------------------")

    # Create XEMBRA instance
    xembra = XEMBRA()

    # Start autonomous cycle thread
    auto_thread = threading.Thread(
        target=run_autonomous_cycle,
        args=(xembra,),
        daemon=True
    )
    auto_thread.start()

    # Start live autonomous output watcher
    watcher_thread = threading.Thread(
        target=autonomous_output_watcher,
        args=(xembra,),
        daemon=True
    )
    watcher_thread.start()

    # Main input loop
    while True:
        try:
            prompt = expressive_prompt(xembra.identity_state, xembra.emotional_state)
            user_input = input(prompt).strip()

            reply = handle_command(xembra, user_input)

            print(f"\n✧ {reply}\n")

        except KeyboardInterrupt:
            print("\n☾  XEMBRA shutting down…\n")
            break

        except Exception as e:
            print(f"[TERMINAL ERROR] {e}")
            time.sleep(1)

# ============================================================
# ENTRY POINT
# ============================================================

if __name__ == "__main__":
    run_terminal()
