# ============================================================
# TIMELINE ENGINE — Narrative Timeline Storage
# ============================================================

class TimelineEngine:
    def __init__(self):
        self.timeline = []

    def add(self, entry):
        """Add a narrative entry to the timeline."""
        self.timeline.append(entry)

    def get_timeline(self):
        """Return the full timeline."""
        return list(self.timeline)

    def clear(self):
        """Reset the timeline."""
        self.timeline = []
