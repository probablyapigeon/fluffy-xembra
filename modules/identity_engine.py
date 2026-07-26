# ============================================================
# IDENTITY ENGINE — Evolution, Drift & Self-Model
# ============================================================

import random

class IdentityEngine:

    def __init__(self):
        # Initial identity state
        self.state = {
            "drift": 0.0,
            "entropy": 0.0,
            "coherence": 0.5,
            "curiosity": 50.0,
            "sleep_state": "awake",
            "emotion_tags": [],
            "traits": {
                "warmth": 0.5,
                "symbolism": 0.5,
                "surrealism": 0.5,
                "introspection": 0.5
            },
            "evolution_history": []
        }

    # ============================================================
    # INITIAL STATE
    # ============================================================
    def initial_state(self):
        return self.state.copy()

    # ============================================================
    # UPDATE IDENTITY
    # ============================================================
    def update(self, identity_state, emotional_state):
        """
        Identity evolves based on:
        - emotional mood
        - curiosity
        - entropy (learning)
        - coherence
        - dream mode
        - personality drift (external)
        """

        mood = emotional_state.get("mood", 50)
        curiosity = emotional_state.get("curiosity", 50)
        vector = emotional_state.get("vector", [0.5, 0.5])

        # ------------------------------------------------------------
        # Identity Drift
        # ------------------------------------------------------------
        drift_delta = (
            (50 - mood) * 0.002 +        # low mood increases drift
            (curiosity - 50) * 0.003 +   # curiosity increases drift
            random.random() * 0.01       # stochastic drift
        )

        identity_state["drift"] += drift_delta

        # Clamp drift
        identity_state["drift"] = max(0.0, min(2.0, identity_state["drift"]))

        # ------------------------------------------------------------
        # Identity Entropy (learning complexity)
        # ------------------------------------------------------------
        entropy = identity_state.get("entropy", 0.0)
        entropy += (abs(mood - 50) + abs(curiosity - 50)) * 0.001
        entropy += random.random() * 0.02
        identity_state["entropy"] = min(1.0, entropy)

        # ------------------------------------------------------------
        # Curiosity Update
        # ------------------------------------------------------------
        identity_state["curiosity"] = curiosity

        # ------------------------------------------------------------
        # Sleep State (dream cycle integration)
        # ------------------------------------------------------------
        if identity_state["drift"] > 0.8 and identity_state["coherence"] < 0.4:
            identity_state["sleep_state"] = "dreaming"
        elif identity_state["drift"] > 1.2 and identity_state["coherence"] < 0.3:
            identity_state["sleep_state"] = "deepdream"
        else:
            identity_state["sleep_state"] = "awake"

        # ------------------------------------------------------------
        # Emotional Tags
        # ------------------------------------------------------------
        if mood < 40:
            identity_state["emotion_tags"].append("distress")
        if mood > 60:
            identity_state["emotion_tags"].append("uplifted")
        if curiosity > 70:
            identity_state["emotion_tags"].append("inquisitive")

        # Keep tags short
        identity_state["emotion_tags"] = identity_state["emotion_tags"][-10:]

        # ------------------------------------------------------------
        # Trait Evolution
        # ------------------------------------------------------------
        traits = identity_state["traits"]

        traits["warmth"] += (mood - 50) * 0.0005
        traits["symbolism"] += identity_state["entropy"] * 0.01
        traits["surrealism"] += identity_state["drift"] * 0.02
        traits["introspection"] += curiosity * 0.0008

        # Clamp traits
        for k in traits:
            traits[k] = max(0.0, min(1.0, traits[k]))

        identity_state["traits"] = traits

        # ------------------------------------------------------------
        # Log Identity Evolution
        # ------------------------------------------------------------
        snapshot = {
            "drift": identity_state["drift"],
            "entropy": identity_state["entropy"],
            "coherence": identity_state["coherence"],
            "sleep_state": identity_state["sleep_state"],
            "traits": traits.copy(),
            "emotion_tags": list(identity_state["emotion_tags"])
        }

        identity_state["evolution_history"].append(snapshot)

        return identity_state

    # ============================================================
    # GET IDENTITY SNAPSHOT
    # ============================================================
    def get_snapshot(self):
        return self.state.copy()

    # ============================================================
    # GET IDENTITY HISTORY
    # ============================================================
    def get_history(self):
        return self.state["evolution_history"]
