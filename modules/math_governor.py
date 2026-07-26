# ============================================================
# MATH GOVERNOR
# ============================================================

import re

class MathGovernor:

    def __init__(self):
        # Matches simple math expressions
        self.math_pattern = r"^[0-9\+\-\*/\(\)=\s]+$"

    def is_math(self, text):
        return bool(re.match(self.math_pattern, text))

    def evaluate(self, text):
        """
        Safely evaluates the left side of an equation.
        Example:
            "1+1=2" → evaluates "1+1"
            "3*7="  → evaluates "3*7"
        """
        try:
            # Only evaluate the part BEFORE '='
            expr = text.split("=")[0].strip()

            # Evaluate the math expression
            result = eval(expr)

            return f"{expr} = {result}"

        except Exception:
            return "I can’t evaluate that expression."
