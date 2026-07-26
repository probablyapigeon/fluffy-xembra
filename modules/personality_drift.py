# ============================================================
# PERSONALITY DRIFT ENGINE
# ============================================================

import random

class PersonalityDriftEngine:

    def __init__(self):
        # Long-term personality traits (0–100)
        self.traits = {
            "openness": 50,
            "stability": 50,
            "expressiveness": 50,
            "sensitivity": 50,
            "assertiveness": 50
        }

        # Drift history for autobiographical memory
        self.history = []

    # ============================================================
    # PERSONALITY DRIFT COMPUTATION
    # ============================================================
    def compute(self, emotional_state, identity_state, learning_engine):
        """
        Updates personality traits based on:
        - emotional mood
        - curiosity
        - identity drift
        - learning entropy
        """

        mood = emotional_state.get("mood", 50)
        curiosity = emotional_state.get("curiosity", 50)
        identity_drift = identity_state.get("drift", 0.0)
        entropy = getattr(learning_engine, "entropy", 0.5)

        # ------------------------------------------------------------
        # Drift logic
        # ------------------------------------------------------------

        # Openness increases with curiosity
        self.traits["openness"] += (curiosity - 50) * 0.05

        # Stability decreases with low mood
        self.traits["stability"] += (mood - 50) * 0.04

        # Expressiveness increases with emotional intensity
        emotional_intensity = abs(mood - 50) + abs(curiosity - 50)
        self.traits["expressiveness"] += emotional_intensity * 0.03

        # Sensitivity increases with identity drift
        self.traits["sensitivity"] += identity_drift * 2.0

        # Assertiveness increases with learning entropy
        self.traits["assertiveness"] += entropy * 1.5

        # ------------------------------------------------------------
        # Clamp values
        # ------------------------------------------------------------
        for k in self.traits:
            self.traits[k] = max(0, min(100, self.traits[k]))

        # ------------------------------------------------------------
        # Log drift event
        # ------------------------------------------------------------
        drift_event = {
            "traits": self.traits.copy(),
            "mood": mood,
            "curiosity": curiosity,
            "identity_drift": identity_drift,
            "entropy": entropy
        }

        self.history.append(drift_event)

        return self.traits

    # ============================================================
    # GET PERSONALITY SNAPSHOT
    # ============================================================
    def get_snapshot(self):
        return self.traits.copy()

    # ============================================================
    # GET DRIFT HISTORY
    # ============================================================
    def get_history(self):
        return self.history
