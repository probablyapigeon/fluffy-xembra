"""XEMBRA state object: drift, entropy, coherence, dream residue.
Simple dataclass to hold internal state and helpers.
"""
from dataclasses import dataclass, field
from typing import Optional
import random

@dataclass
class XembraState:
    drift: float = 0.0
    entropy: float = 0.2
    coherence: float = 0.8
    dream_residue: float = 0.0
    step_count: int = 0
    rng_seed: Optional[int] = None
    rng: random.Random = field(init=False, repr=False)

    def __post_init__(self):
        self.rng = random.Random(self.rng_seed)

    def reset(self, seed: Optional[int] = None) -> None:
        self.drift = 0.0
        self.entropy = 0.2
        self.coherence = 0.8
        self.dream_residue = 0.0
        self.step_count = 0
        self.rng_seed = seed
        self.rng = random.Random(seed)

    @staticmethod
    def _clip(x: float, lo: float = 0.0, hi: float = 1.0) -> float:
        return max(lo, min(hi, x))
