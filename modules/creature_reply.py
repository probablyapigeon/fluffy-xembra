# ============================================================
# CREATURE REPLY ENGINE — Expressive & Symbolic (N2)
# ============================================================

from drift_speech import generate_drift_speech
from dream_speech import generate_dream_speech
from internal_thought import generate_internal_thought
from companion_reaction import generate_companion_reaction
from memory_dialogue import generate_memory_dialogue
from self_identity import generate_self_identity_line
from emotional_tone import update_emotional_tone
from world_interaction import process_world_event

def generate_reply(xembra, user_input):
    """
    Main expressive reply engine.
    Blends:
    - drift speech
    - dream speech
    - internal thought
    - companion reaction
    - memory dialogue
    - identity line
    - emotional tone update
    """

    identity_state = xembra.identity_state
    emotional_state = xembra.emotional_state
    learning_engine = xembra.learning_engine

    # Feed word into learning engine
    learning_engine.ingest_word(user_input)

    emotional_state = update_emotional_tone(
        identity_state,
        emotional_state,
        learning_engine,
        emotional_state["mood"],
        emotional_state["curiosity"],
        xembra.attachment_state
    )
    xembra.emotional_state = emotional_state

    # Memory dialogue
    memory_line = generate_memory_dialogue(identity_state, learning_engine)

    # Identity line
    identity_line = generate_self_identity_line(identity_state, emotional_state, learning_engine)

    # Companion reaction
    reaction = generate_companion_reaction(
        identity_state,
        learning_engine,
        emotional_state["mood"],
        emotional_state["curiosity"],
        xembra.attachment_state
    )

    # Drift speech (awake surrealism)
    drift_line = generate_drift_speech(identity_state, learning_engine)

    # Dream speech (if dreaming)
    dream_line = ""
    if identity_state.get("sleep_state") in ["dreaming", "deepdream"]:
        dream_line = generate_dream_speech(identity_state, learning_engine)

    # Internal thought (soft introspection)
    inner_line = generate_internal_thought(
        identity_state,
        learning_engine,
        emotional_state["mood"],
        emotional_state["curiosity"]
    )

    # Blend reply based on sleep state
    sleep_state = identity_state.get("sleep_state", "awake")

    if sleep_state == "awake":
        return f"{reaction}\n{identity_line}\n{memory_line}\n{drift_line}\n{inner_line}"

    if sleep_state == "dreaming":
        return f"{dream_line}\n{identity_line}\n{memory_line}\n{inner_line}"

    if sleep_state == "deepdream":
        return f"{dream_line}\n{identity_line}\n{memory_line}"

    return reaction
