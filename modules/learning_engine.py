# ============================================================
# LEARNING ENGINE — Entropy, Memory, Cognitive Growth (Stable)
# ============================================================

import random

class LearningEngine:

    def __init__(self):
        self.memory = []
        self.entropy = 0.0
        self.learning_history = []
        self.recent_word = None

    # ============================================================
    # UPDATE LEARNING STATE
    # ============================================================
    def update(self, user_input):
        """
        Learning increases based on:
        - novelty of input
        - emotional intensity
        - world-state complexity
        - randomness (stochastic learning)
        """

        # Extract last meaningful word
        tokens = user_input.strip().split()
        if tokens:
            self.recent_word = tokens[-1].lower()

        # Memory fragment
        fragment = {
            "fragment": user_input,
            "strength": random.uniform(0.2, 1.0)
        }
        self.memory.append(fragment)

        # Entropy update
        novelty = len(set(tokens)) / max(1, len(tokens))
        randomness = random.random() * 0.05

        self.entropy += novelty * 0.1 + randomness
        self.entropy = min(1.0, self.entropy)

        # Log learning event
        snapshot = {
            "entropy": self.entropy,
            "fragment": fragment,
            "memory_size": len(self.memory)
        }

        self.learning_history.append(snapshot)
        return snapshot

    # ============================================================
    # REQUIRED BY MEMORY CONSOLIDATION
    # ============================================================
    def get_recent_word(self):
        """Return the most recently processed word."""
        return self.recent_word

    def store_memory(self, entry):
        """Store symbolic memory fragments."""
        self.memory.append(entry)

    # ============================================================
    # LEARNING EXPRESSION (FOR LLM)
    # ============================================================
    def express(self):
        """Produces a learning expression object for the LLM."""

        if self.entropy < 0.2:
            return {
                "level": "low",
                "description": "Learning is slow and steady, with small fragments forming."
            }

        if self.entropy < 0.5:
            return {
                "level": "moderate",
                "description": "Patterns begin to emerge as new information integrates."
            }

        if self.entropy < 0.8:
            return {
                "level": "high",
                "description": "Learning accelerates, weaving complex associations."
            }

        return {
            "level": "surge",
            "description": "A surge of learning reshapes internal structure and meaning."
        }

    # ============================================================
    # SUMMARY + HISTORY
    # ============================================================
    def get_learning_summary(self):
        return {
            "entropy": self.entropy,
            "memory_size": len(self.memory),
            "recent_fragments": self.memory[-5:]
        }

    def get_history(self):
        return self.learning_history
