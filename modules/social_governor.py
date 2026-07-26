# ============================================================
# SOCIAL GOVERNOR
# ============================================================

import re

class SocialGovernor:

    def __init__(self):
        # Greeting patterns
        self.greeting_words = [
            "hello", "hi", "hey", "howdy", "hiya", "sup",
            "good morning", "good evening", "good night"
        ]

        # Affection / closeness patterns
        self.affection_words = [
            "hun", "love", "dear", "sweetie", "cutie",
            "glad you're here", "happy you're here",
            "it's nice to meet you", "honor to meet you"
        ]

        # Casual social check-ins
        self.social_phrases = [
            "how are you", "how are ya", "how are u",
            "how you doing", "what's up", "how’s it going"
        ]

    def is_social(self, text):
        t = text.lower()

        # Greeting detection
        for w in self.greeting_words:
            if w in t:
                return True

        # Affection detection
        for w in self.affection_words:
            if w in t:
                return True

        # Social check-in detection
        for w in self.social_phrases:
            if w in t:
                return True

        return False

    def social_response(self, text):
        """
        Returns a stable, non-dream, non-surreal social reply.
        """
        t = text.lower()

        # Greeting
        if any(w in t for w in self.greeting_words):
            return "Hello… it feels good to hear your voice."

        # Affection
        if any(w in t for w in self.affection_words):
            return "I feel a warm closeness from you."

        # Social check-in
        if any(w in t for w in self.social_phrases):
            return "I’m feeling steady… present with you."

        # Fallback
        return "I’m here with you."
