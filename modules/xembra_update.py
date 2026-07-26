"""State update mechanics for XEMBRA.
Expose `update_step(state)` which mutates state and returns a short narrative line.
"""
from .xembra_state import XembraState
from .xembra_narrative import compose_narrative


def apply_drift(state: XembraState) -> None:
    state.drift += state.rng.uniform(-0.01, 0.02)
    state.coherence = XembraState._clip(state.coherence - 0.003 * state.drift)
    state.entropy = XembraState._clip(state.entropy + 0.002 * abs(state.drift))


def dream_cycle(state: XembraState) -> None:
    change = (state.entropy - 0.5) * 0.05
    state.dream_residue = XembraState._clip(state.dream_residue + change + state.rng.uniform(-0.01, 0.01))


def disturb(state: XembraState, magnitude: float = 0.05) -> None:
    state.entropy = XembraState._clip(state.entropy + magnitude * state.rng.uniform(0.5, 1.5))
    state.coherence = XembraState._clip(state.coherence - magnitude * state.rng.uniform(0.2, 1.0))


def update_step(state: XembraState) -> str:
    """Advance the internal dynamics one tick and return a narrative line."""
    state.step_count += 1
    apply_drift(state)
    dream_cycle(state)

    # small stochastic fluctuations
    state.entropy = XembraState._clip(state.entropy + state.rng.uniform(-0.02, 0.03))
    state.coherence = XembraState._clip(state.coherence + state.rng.uniform(-0.02, 0.02))

    # occasional disturbance
    if state.rng.random() < 0.03:
        disturb(state, 0.1)

    return compose_narrative(state)
