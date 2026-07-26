# ============================================================
# CONTEXT GOVERNOR
# ============================================================

class ContextGovernor:

    def __init__(self):
        self.last_topic = None

    def detect_topic(self, text):
        # crude topic detection
        if any(w in text.lower() for w in ["math", "+", "-", "*", "/", "="]):
            return "math"
        if "how" in text.lower():
            return "how"
        if "music" in text.lower():
            return "music"
        return "general"

    def breaks_context(self, text):
        new_topic = self.detect_topic(text)

        if self.last_topic is None:
            self.last_topic = new_topic
            return False

        if new_topic != self.last_topic:
            self.last_topic = new_topic
            return True

        return False
