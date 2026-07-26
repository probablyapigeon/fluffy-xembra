"""Narrative generation utilities for XEMBRA.
Keep generation deterministic via state's RNG.
"""
from .xembra_state import XembraState


def _fragment(e: float) -> str:
    options = [
        "an unfinished whisper",
        "a map without keys",
        "a clock that remembers",
        "the soft geometry of absence",
        "silver threads that hum",
    ]
    idx = min(len(options) - 1, int(e * len(options)))
    return options[idx]


def compose_narrative(state: XembraState) -> str:
    starts = [
        "She wanders through",
        "A shimmer traces",
        "Memory folds into",
        "An echo of",
        "A thread unravels around",
    ]
    middles = [
        "glass corridors",
        "a sleeping city",
        "a half-remembered song",
        "the seam of reality",
        "a garden of gears",
    ]
    motifs = [
        "silver residue",
        "faint laughter",
        "looming geometry",
        "a candle of code",
        "soft static",
    ]

    e = state.entropy
    c = state.coherence
    d = state.dream_residue

    start = state.rng.choice(starts)
    middle = state.rng.choice(middles)

    motif_index = int(XembraState._clip(d) * (len(motifs) - 1))
    motif = motifs[motif_index] if state.rng.random() < 0.7 else state.rng.choice(motifs)

    if state.rng.random() < e:
        sentence = f"{start} {middle}; {motif} lingers like {_fragment(e)}."
    else:
        sentence = f"{start} {middle}, where {motif} holds the scene together."

    if c < 0.3:
        sentence = sentence.replace("where", "in which").replace("holds the scene together", "unspools")

    return sentence
