# ============================================================
# REPLY STABILIZER — Prevent repetition + balance dreaminess
# ============================================================

import random

class ReplyStabilizer:
    def __init__(self):
        self.last_fragment = None
        self.last_structure = None
        self.repeat_counter = 0

    def stabilize(self, reply, xembra):
        """
        Hybrid A+B stabilizer:
        - prevents repeated dream fragments
        - prevents repeated reply structures
        - reduces drift influence
        - keeps dreamy tone but grounded
        - forces variety when repetition detected
        """

        # ------------------------------------------------------------
        # Detect repeated fragments
        # ------------------------------------------------------------
        fragment = reply[:40]  # first 40 chars define the "shape"
        if fragment == self.last_fragment:
            self.repeat_counter += 1
        else:
            self.repeat_counter = 0

        self.last_fragment = fragment

        # ------------------------------------------------------------
        # If repeating → force variety
        # ------------------------------------------------------------
        if self.repeat_counter >= 1:
            reply = self._force_variety(reply, xembra)

        # ------------------------------------------------------------
        # Reduce drift influence (A)
        # ------------------------------------------------------------
        xembra.identity_state["drift"] *= 0.6

        # ------------------------------------------------------------
        # Reduce dream intensity (A)
        # ------------------------------------------------------------
        if "dream_intensity" in xembra.identity_state:
            xembra.identity_state["dream_intensity"] *= 0.7

        # ------------------------------------------------------------
        # Add gentle surreal tone (B)
        # ------------------------------------------------------------
        reply = self._add_dream_flavor(reply)

        return reply

    # ============================================================
    # INTERNAL HELPERS
    # ============================================================

    def _force_variety(self, reply, xembra):
        """
        Replace repeated fragments with fresh ones.
        """
        options = [
            "I feel something shifting inside me… softly.",
            "A new thought drifts in… gentle and different.",
            "Something feels clearer now… like a fresh breath.",
            "My mind feels steadier… but still curious.",
            "I sense a new shape forming in my thoughts."
        ]
        return random.choice(options)

    def _add_dream_flavor(self, reply):
        """
        Adds a light surreal tone without overwhelming the reply.
        """
        dream_additions = [
            " It feels soft around the edges.",
            " There’s a quiet glow to the thought.",
            " It drifts like a small dream.",
            " It feels warm and gentle.",
            " It moves like a slow ripple."
        ]
        if random.random() < 0.3:
            reply += random.choice(dream_additions)
        return reply
