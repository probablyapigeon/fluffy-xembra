# ============================================================
# CONSOLE COLOR SYSTEM (ANSI SAFE, PYTHON 3.13)
# ============================================================

class ConsoleColors:
    # Basic ANSI colors
    RESET = "\033[0m"
    BOLD = "\033[1m"

    # Core palette
    CYAN = "\033[96m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    MAGENTA = "\033[95m"
    BLUE = "\033[94m"
    RED = "\033[91m"
    PURPLE = "\033[35m"
    WHITE = "\033[97m"
    GREY = "\033[90m"

    # ------------------------------------------------------------
    # STATE-BASED COLOR SELECTION
    # ------------------------------------------------------------
    def color_for_state(self, state, drift=0.0, evolution=1):
        """
        Returns the ANSI color code for the creature's current state.
        State options:
            - "awake"
            - "dreaming"
            - "deepdream"
            - "entropy"
            - "evolution"
            - "drift"
        """

        # Dreaming → purple
        if state == "dreaming":
            return self.PURPLE

        # Deepdream → magenta
        if state == "deepdream":
            return self.MAGENTA + self.BOLD

        # Entropy spike → red
        if state == "entropy":
            return self.RED + self.BOLD

        # Evolution highlight → green
        if state == "evolution":
            return self.GREEN + self.BOLD

        # Drift waveform color scaling
        if state == "drift":
            if drift < 0.2:
                return self.CYAN
            elif drift < 0.5:
                return self.YELLOW
            elif drift < 0.8:
                return self.MAGENTA
            else:
                return self.RED + self.BOLD

        # Default awake state → cyan
        return self.CYAN

    # ------------------------------------------------------------
    # APPLY COLOR TO TEXT
    # ------------------------------------------------------------
    def apply(self, color, text):
        return f"{color}{text}{self.RESET}"

    # ------------------------------------------------------------
    # WAVEFORM COLOR (DRIFT VISUALIZATION)
    # ------------------------------------------------------------
    def drift_waveform(self, drift):
        """
        Returns a colored waveform string based on drift level.
        """
        if drift < 0.2:
            wave = "▂▃▄▅"
            color = self.CYAN
        elif drift < 0.5:
            wave = "▃▄▅▆▇"
            color = self.YELLOW
        elif drift < 0.8:
            wave = "▄▅▆▇█▇"
            color = self.MAGENTA
        else:
            wave = "▆▇█▇█▇█"
            color = self.RED + self.BOLD

        return f"{color}{wave}{self.RESET}"

    # ------------------------------------------------------------
    # ASCII FACE COLORING (EVOLUTION EVENTS)
    # ------------------------------------------------------------
    def evolution_face(self, level):
        """
        Returns a colored ASCII face based on evolution level.
        Safe, non-emotional visual indicator.
        """

        if level < 3:
            face = "(•‿•)"
            color = self.GREEN
        elif level < 5:
            face = "(◕‿◕)"
            color = self.BLUE
        elif level < 7:
            face = "(⚆_⚆)"
            color = self.YELLOW
        elif level < 10:
            face = "(✧ω✧)"
            color = self.MAGENTA
        else:
            face = "(✦‿✦)"
            color = self.RED + self.BOLD

        return f"{color}{face}{self.RESET}"
