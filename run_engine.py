"""Simple Engine wrapper for XEMBRA.
NOTE: Replace this file with your own run_engine.py if you have a custom version — this is a friendly stub that is fully functional.
"""
from modules.xembra_state import XembraState
from modules.xembra_update import update_step


class Engine:
    """Run the narrative loop and expose a small programmatic API."""

    def __init__(self, seed: int | None = None):
        self.state = XembraState(rng_seed=seed)

    def step(self) -> str:
        """Advance one tick and return narrative line."""
        return update_step(self.state)

    def run_n(self, n: int) -> list[str]:
        lines = []
        for _ in range(max(0, int(n))):
            lines.append(self.step())
        return lines

    def reset(self, seed: int | None = None) -> None:
        self.state.reset(seed)
