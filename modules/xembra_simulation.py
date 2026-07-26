# ============================================================
# XEMBRA SIMULATION — Full Autonomous + Interactive Loop
# ============================================================

import time
import random
import threading

from xembra import XEMBRA
from autonomous_cycle import run_autonomous_cycle
from memory_visualizer import MemoryVisualizer


# ------------------------------------------------------------
# OPTIONAL WORLD EVENT STREAM
# ------------------------------------------------------------

WORLD_EVENTS = [
    {"type": "sound", "name": "wind chime"},
    {"type": "environment", "name": "rain"},
    {"type": "object", "name": "mirror"},
    {"type": "light", "name": "neon glow"},
    {"type": "sound", "name": "soft hum"},
    {"type": "environment", "name": "fog"},
]


# ------------------------------------------------------------
# AUTONOMOUS BACKGROUND THREAD
# ------------------------------------------------------------

def start_autonomous_thread(xembra, world_events=None, interval=3.0):
    """
    Runs XEMBRA's autonomous cycle continuously in the background.
    """

    def loop():
        while True:
            result = run_autonomous_cycle(xembra, world_events=world_events, interval=interval)

            if result:
                if result["spontaneous_thought"]:
                    print(f"\n🜁 XEMBRA (thought): {result['spontaneous_thought']}")
                if result["world_reaction"]:
                    print(f"\n🜁 XEMBRA (world): {result['world_reaction']}")

            time.sleep(1.0)

    thread = threading.Thread(target=loop, daemon=True)
    thread.start()


# ------------------------------------------------------------
# MAIN SIMULATION LOOP
# ------------------------------------------------------------

def run_simulation():
    print("============================================================")
    print("                 X E M B R A   S I M U L A T I O N")
    print("============================================================")
    print("Simulation Controls:")
    print("  /style <name>       — change speech style")
    print("  /sense <object>     — send world event")
    print("  /memory             — show memory summary")
    print("  /dreams             — show dream digest")
    print("  /identity           — show identity timeline")
    print("  /emotion            — show emotional timeline")
    print("  /world              — show world event history")
    print("  /interactions       — show user interaction history")
    print("  /quit               — exit simulation")
    print("------------------------------------------------------------")

    xembra = XEMBRA(style="neutral")

    # Start autonomous background thinking
    start_autonomous_thread(xembra, world_events=WORLD_EVENTS, interval=3.0)

    # Interactive loop
    while True:
        user_input = input("\nYou: ").strip()

        # --------------------------------------------------------
        # COMMANDS
        # --------------------------------------------------------

        if user_input.startswith("/style"):
            _, style = user_input.split(" ", 1)
            xembra.set_style(style)
            print(f"XEMBRA style set to: {style}")
            continue

        if user_input.startswith("/sense"):
            _, obj = user_input.split(" ", 1)
            event = {"type": "object", "name": obj}
            reaction = xembra.sense(event)
            print(f"XEMBRA (world): {reaction}")
            continue

        if user_input == "/memory":
            viz = MemoryVisualizer()
            print(viz.summarize())
            continue

        if user_input == "/dreams":
            viz = MemoryVisualizer()
            print(viz.dream_digest())
            continue

        if user_input == "/identity":
            viz = MemoryVisualizer()
            print(viz.identity_graph())
            continue

        if user_input == "/emotion":
            viz = MemoryVisualizer()
            print(viz.emotional_timeline())
            continue

        if user_input == "/world":
            viz = MemoryVisualizer()
            print(viz.world_summary())
            continue

        if user_input == "/interactions":
            viz = MemoryVisualizer()
            print(viz.interaction_summary())
            continue

        if user_input == "/quit":
            print("Exiting XEMBRA simulation…")
            break

        # --------------------------------------------------------
        # NORMAL USER MESSAGE
        # --------------------------------------------------------
        reply = xembra.talk(user_input)
        print(f"XEMBRA: {reply}")


# ------------------------------------------------------------
# ENTRY POINT
# ------------------------------------------------------------

if __name__ == "__main__":
    run_simulation()
