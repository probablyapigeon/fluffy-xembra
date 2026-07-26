# ============================================================
# AUTONOMOUS CYCLE — Stable + Expressive (N2)
# ============================================================

import time
import threading

from autonomous_thought import generate_autonomous_thought
from internal_thought import generate_internal_thought
from memory_consolidation import consolidate_memory
from identity_drift import update_identity_drift
from mutate_personality import mutate_personality

def run_autonomous_cycle(xembra):
    def loop():
        while xembra.autonomous:
            try:
                # DEBUG: entropy check
                print("AUTONOMOUS ENTROPY EXISTS:", "entropy" in xembra.identity_state)

                drift = update_identity_drift(
                    xembra.identity_state,
                    xembra.emotional_state,
                    xembra.learning_engine
                )

                mutate_personality(xembra.identity_state, xembra.emotional_state)

                thought = generate_autonomous_thought(
                    xembra.identity_state,
                    xembra.emotional_state,
                    xembra.learning_engine
                )

                internal = generate_internal_thought(
                    xembra.identity_state,
                    xembra.learning_engine,
                    xembra.emotional_state["mood"],
                    xembra.emotional_state["curiosity"]
                )

                consolidate_memory(
                    xembra.identity_state,
                    xembra.learning_engine,
                    xembra.emotional_state
                )

                xembra.logs.append(f"[AUTO] {thought}")
                xembra.logs.append(f"[INNER] {internal}")

            except Exception as e:
                print(f"[AUTONOMOUS ERROR] {e}")

            time.sleep(3.0)

    thread = threading.Thread(target=loop, daemon=True)
    thread.start()
