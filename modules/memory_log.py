# ============================================================
# MEMORY LOG — Stable & Coherent Version (B1)
# ============================================================

import time


class MemoryLog:
    def __init__(self):

        # Core logs
        self.learning_log = []
        self.identity_log = []
        self.emotion_log = []
        self.interaction_log = []
        self.world_log = []
        self.dream_fragments = []

    # ============================================================
    # STORE FUNCTIONS
    # ============================================================

    def store_learning(self, learning_engine):
        """
        Stores a snapshot of the learning engine state.
        """
        entry = {
            "time": time.time(),
            "vocab_size": len(learning_engine.vocab),
            "concepts": list(learning_engine.concepts)[-10:],  # last 10 concepts
            "entropy": learning_engine.entropy
        }
        self.learning_log.append(entry)

        if len(self.learning_log) > 200:
            self.learning_log.pop(0)

    def store_identity(self, identity_state):
        """
        Stores identity drift, coherence, sleep state, etc.
        """
        entry = {
            "time": time.time(),
            "drift": identity_state.get("drift", 0.0),
            "coherence": identity_state.get("coherence", 1.0),
            "sleep_state": identity_state.get("sleep_state", "awake"),
            "identity_age": identity_state.get("identity_age", 0.0),
            "speech_style": identity_state.get("speech_style", "NEUTRAL")
        }
        self.identity_log.append(entry)

        if len(self.identity_log) > 200:
            self.identity_log.pop(0)

        # Track dream fragments
        if entry["sleep_state"] in ("dreaming", "deepdream"):
            frag = identity_state.get("dream_fragment")
            if frag:
                self.dream_fragments.append(frag)
                if len(self.dream_fragments) > 200:
                    self.dream_fragments.pop(0)

    def store_emotion(self, emotional_state):
        """
        Stores mood, curiosity, closeness.
        """
        entry = {
            "time": time.time(),
            "mood": emotional_state.get("mood", 50.0),
            "curiosity": emotional_state.get("curiosity", 50.0),
            "closeness": emotional_state.get("closeness", 0.5)
        }
        self.emotion_log.append(entry)

        if len(self.emotion_log) > 200:
            self.emotion_log.pop(0)

    def store_interaction(self, text):
        """
        Stores user or autonomous interactions.
        """
        entry = {
            "time": time.time(),
            "text": text
        }
        self.interaction_log.append(entry)

        if len(self.interaction_log) > 300:
            self.interaction_log.pop(0)

    def store_world_event(self, event):
        """
        Stores world-sense events.
        """
        entry = {
            "time": time.time(),
            "event": event
        }
        self.world_log.append(entry)

        if len(self.world_log) > 100:
            self.world_log.pop(0)

    # ============================================================
    # SUMMARY OUTPUTS
    # ============================================================

    def summary(self):
        """
        Returns a compact summary of memory state.
        """
        return (
            f"Memory Summary:\n"
            f"- Learning entries: {len(self.learning_log)}\n"
            f"- Identity entries: {len(self.identity_log)}\n"
            f"- Emotion entries: {len(self.emotion_log)}\n"
            f"- Interactions: {len(self.interaction_log)}\n"
            f"- World events: {len(self.world_log)}\n"
            f"- Dream fragments: {len(self.dream_fragments)}"
        )

    def dump(self):
        """
        Returns full logs (raw).
        """
        return {
            "learning": self.learning_log,
            "identity": self.identity_log,
            "emotion": self.emotion_log,
            "interactions": self.interaction_log,
            "world": self.world_log,
            "dream_fragments": self.dream_fragments
        }

    # ============================================================
    # TIMELINES
    # ============================================================

    def identity_timeline(self):
        """
        Returns a readable identity evolution timeline.
        """
        lines = []
        for entry in self.identity_log[-50:]:
            t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(entry["time"]))
            lines.append(
                f"[{t}] drift={entry['drift']:.2f}, "
                f"coherence={entry['coherence']:.2f}, "
                f"sleep={entry['sleep_state']}, "
                f"style={entry['speech_style']}"
            )
        return "\n".join(lines)

    def emotion_timeline(self):
        """
        Returns a readable emotional timeline.
        """
        lines = []
        for entry in self.emotion_log[-50:]:
            t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(entry["time"]))
            lines.append(
                f"[{t}] mood={entry['mood']:.2f}, "
                f"curiosity={entry['curiosity']:.2f}, "
                f"closeness={entry['closeness']:.2f}"
            )
        return "\n".join(lines)

    def dream_digest(self):
        """
        Returns the last 10 dream fragments.
        """
        lines = []
        for frag in self.dream_fragments[-10:]:
            t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
            lines.append(f"[{t}] {frag}")
        return "\n".join(lines)
