# ============================================================
# LEARNING ENGINE — Stable & Coherent Version (B1)
# ============================================================

import random
import time


class LearningEngine:
    def __init__(self):

        # Core memory stores
        self.vocab = set()
        self.concepts = set()
        self.phrases = set()

        # World events
        self.world_events = []

        # Logs
        self.internal_log = []

        # Entropy (controls dream blending)
        self.entropy = 0.05

        # Recent memory buffers
        self.recent_words = []
        self.recent_phrases = []
        self.memory_fragments = []

    # ============================================================
    # BASIC LOGGER (required by dream_cycle)
    # ============================================================

    def log(self, message):
        timestamp = time.time()
        self.internal_log.append((timestamp, message))

    # ============================================================
    # LEARNING PIPELINE
    # ============================================================

    def learn(self, text):

        # Clean input
        if not text or not isinstance(text, str):
            return

        # Tokenize
        words = [w.strip() for w in text.split() if w.strip()]

        # Store recent words
        for w in words:
            self.vocab.add(w)
            self.recent_words.append(w)
            if len(self.recent_words) > 50:
                self.recent_words.pop(0)

        # Concepts = unique words
        for w in words:
            self.concepts.add(w)

        # Phrase learning
        for i in range(len(words) - 1):
            phrase = f"{words[i]} {words[i+1]}"
            self.phrases.add(phrase)
            self.recent_phrases.append(phrase)
            if len(self.recent_phrases) > 50:
                self.recent_phrases.pop(0)

        # Memory fragments
        if words:
            frag = random.choice(words)
            self.memory_fragments.append(frag)
            if len(self.memory_fragments) > 100:
                self.memory_fragments.pop(0)

        # Entropy adjusts slightly with learning
        self.entropy = min(0.25, self.entropy + 0.005)

        self.log(f"LEARNED: {text}")

    # ============================================================
    # WORLD EVENTS
    # ============================================================

    def store_world_event(self, event):
        self.world_events.append(event)
        if len(self.world_events) > 50:
            self.world_events.pop(0)
        self.log(f"WORLD_EVENT: {event}")

    # ============================================================
    # MEMORY FRAGMENTS
    # ============================================================

    def get_memory_fragment(self):
        if not self.memory_fragments:
            return None
        return random.choice(self.memory_fragments)

    # ============================================================
    # RECENT WORD / PHRASE ACCESSORS
    # ============================================================

    def get_recent_word(self):
        if not self.recent_words:
            return ""
        return self.recent_words[-1]

    def get_recent_phrase(self):
        if not self.recent_phrases:
            return ""
        return self.recent_phrases[-1]

    # ============================================================
    # SEQUENCE GENERATOR (stable version)
    # ============================================================

    def generate_sequence(self):
        """
        Generates a stable neural pattern sequence.
        No glitching, no malformed tokens.
        """

        if not self.vocab:
            return ""

        choices = random.sample(list(self.vocab), min(3, len(self.vocab)))
        seq = " → ".join(choices)

        self.log(f"SEQUENCE: {seq}")
        return seq

    # ============================================================
    # DREAM BLEND SUPPORT (stable version)
    # ============================================================

    def dream_blend(self, a, b):
        """
        Stable blend: no empty tokens, no nonsense.
        """

        if not a or not b:
            return a or b

        # Simple stable blend: first half + second half
        mid_a = len(a) // 2
        mid_b = len(b) // 2

        blend = a[:mid_a] + b[mid_b:]

        self.log(f"DREAM_BLEND: {a} + {b} → {blend}")
        return blend
