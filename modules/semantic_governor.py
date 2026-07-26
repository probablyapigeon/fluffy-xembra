# ============================================================
# SEMANTIC GOVERNOR
# ============================================================

import re

class SemanticGovernor:

    def __init__(self):
        self.definition_patterns = [
            r"^the word .+ means",
            r"^the term .+ means",
            r"is defined as",
            r"refers to",
            r"means",
        ]

        self.factual_keywords = [
            "used to",
            "primarily",
            "inquires",
            "describes",
            "refers",
            "means",
            "definition",
            "state of being",
            "method",
            "manner",
            "degree",
            "extent",
        ]

    def requires_semantic_mode(self, text):
        t = text.lower()

        # definition?
        for p in self.definition_patterns:
            if re.search(p, t):
                return True

        # factual?
        for k in self.factual_keywords:
            if k in t:
                return True

        return False
