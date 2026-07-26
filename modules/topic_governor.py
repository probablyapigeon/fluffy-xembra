# ============================================================
# TOPIC GOVERNOR — Handles Named Entities & Subject Matter
# ============================================================

import re

class TopicGovernor:

    def __init__(self):

        # Proper nouns, named entities, historical figures, subjects
        self.topic_patterns = [
            r"\beinstein\b",
            r"\bfurniture\b",
            r"\bcollection\b",
            r"\bgriffin\b",
            r"\bprinceton\b",
            r"\bscientist\b",
            r"\btheory\b",
            r"\bphysics\b",
            r"\brelativity\b",
            r"\bnuclear\b",
            r"\bmanhattan project\b",
            r"\bberlin\b",
            r"\bmercer street\b",
            r"\binnovators\b",
            r"\bicon\b",
            r"\bexhibit\b",
            r"\barchive\b",
            r"\bhistorical\b",
            r"\bcommission\b",
            r"\bconservator\b",
            r"\bpipe\b",
            r"\bpuzzle\b",
            r"\bcompass\b",
            r"\bfield theory\b",
            r"\bpalestine\b",
            r"\bisrael\b",
            r"\bflexner\b",
            r"\bweizmann\b",
            r"\bgriffin\b",
            r"\bcurator\b"
        ]

        # Long factual passages (3+ sentences)
        self.long_text_threshold = 250  # characters

    def is_topic(self, text):
        t = text.lower()

        # Long factual text → topic
        if len(t) > self.long_text_threshold:
            return True

        # Named entity / subject detection
        for pattern in self.topic_patterns:
            if re.search(pattern, t):
                return True

        return False

    def topic_response(self, text):
        """
        Stable, grounded reply for topical content.
        Prevents dream-speech, drift-speech, memory-dialogue.
        """
        return "I’m following the topic you’re exploring… staying steady with you."
