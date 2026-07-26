# ============================================================
# MEMORY GOVERNOR
# ============================================================

class MemoryGovernor:

    def detect_fixation(self, memory_log):
        recent = memory_log.get_recent_interaction()

        if not recent:
            return False

        user_text = recent.get("user", "").lower()

        # if user repeats same word too often, or XEMBRA loops
        fixation_words = ["are", "how", "bb", "music"]

        for w in fixation_words:
            if user_text.count(w) > 2:
                return True

        return False
