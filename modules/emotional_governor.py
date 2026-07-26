# ============================================================
# EMOTIONAL GOVERNOR (UPGRADED)
# ============================================================

import re

class EmotionalGovernor:

    def __init__(self):
        # Negative emotional indicators
        self.emotion_words = [
            "sad", "upset", "hurt", "lonely", "scared",
            "afraid", "anxious", "worried", "overwhelmed",
            "depressed", "angry", "frustrated", "cry",
            "crying", "heartbroken", "tired", "exhausted",
            "stressed", "pain", "hurting"
        ]

        # Positive emotional indicators
        self.positive_words = [
            "happy", "glad", "love", "excited", "joy",
            "delighted", "grateful"
        ]

    # ============================================================
    # EMOTIONAL STATE COMPUTATION
    # ============================================================
    def compute(self, user_input, previous_state):
        """
        Produces an updated emotional_state object.
        Tracks:
        - mood
        - curiosity
        - emotional history
        - emotional vector
        """

        mood = previous_state.get("mood", 50)
        curiosity = previous_state.get("curiosity", 50)
        history = previous_state.get("history", [])

        lowered = user_input.lower()

        # Detect negative emotional triggers
        for w in self.emotion_words:
            if w in lowered:
                mood -= 10
                history.append(f"Detected negative emotion: {w}")

        # Detect positive emotional triggers
        for w in self.positive_words:
            if w in lowered:
                mood += 10
                history.append(f"Detected positive emotion: {w}")

        # Clamp values
        mood = max(0, min(100, mood))
        curiosity = max(0, min(100, curiosity))

        # Simple emotional vector (expand later if needed)
        vector = [mood / 100.0, curiosity / 100.0]

        return {
            "mood": mood,
            "curiosity": curiosity,
            "vector": vector,
            "history": history
        }

    # ============================================================
    # EMOTIONAL STABILIZATION CHECK
    # ============================================================
    def requires_stabilization(self, emotional_state, user_input):
        """
        Returns True if emotional stabilization should override
        the creature pipeline.
        """

        text = user_input.lower()

        # 1. Detect emotional language from the user
        for w in self.emotion_words:
            if w in text:
                return True

        # 2. Detect positive emotional spikes (optional)
        for w in self.positive_words:
            if w in text:
                return True

        # 3. Numeric fallback (your original logic)
        mood = emotional_state.get("mood", 50)
        curiosity = emotional_state.get("curiosity", 50)

        if mood < 30:
            return True

        if curiosity > 85:
            return True

        return False
