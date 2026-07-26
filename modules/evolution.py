# ============================================================
# EVOLUTION EVENT SYSTEM
# Visible evolution upgrades + ASCII faces + color output
# ============================================================

from modules.console_colors import ConsoleColors

class EvolutionSystem:
    def __init__(self):
        self.colors = ConsoleColors()
        self.last_level = 1

    # ------------------------------------------------------------
    # PUBLIC: Called whenever evolution_level changes
    # ------------------------------------------------------------
    def handle_evolution(self, new_level):
        """
        Called by creature_reply or robot loop whenever learning.py
        increases evolution_level. This prints visible evolution events.
        """

        # Only print when evolution actually increases
        if new_level <= self.last_level:
            return

        # Update internal tracker
        self.last_level = new_level

        # Get ASCII face for this level
        face = self.colors.evolution_face(new_level)

        # Build evolution message
        msg = f"[EVOLUTION +{new_level}]"

        # Colorize evolution message
        colored_msg = self.colors.apply(
            self.colors.color_for_state("evolution", evolution=new_level),
            msg
        )

        # Print evolution event
        print(colored_msg)
        print(face)

    # ------------------------------------------------------------
    # OPTIONAL: Get evolution face without printing
    # ------------------------------------------------------------
    def get_face(self, level):
        return self.colors.evolution_face(level)
