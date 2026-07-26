# ============================================================
# DREAM → LLM SURREALISM LAYER
# ============================================================

class DreamSurrealismLayer:

    def expand(self, dream_expression):
        """
        Converts dream expression into surreal narrative cues.
        """

        if not dream_expression:
            return None

        mode = dream_expression.get("mode")
        intensity = dream_expression.get("intensity")
        description = dream_expression.get("description")

        if mode == "dreaming":
            return f"A gentle dream-state emerges: {description}"

        if mode == "deepdream":
            return f"A deepdream unfolds with surreal intensity ({intensity:.2f}): {description}"

        return None
