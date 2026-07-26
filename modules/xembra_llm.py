"""OpenAI integration for XEMBRA.

Provides a thin wrapper around the OpenAI Python client and a helper that
turns an engine state into a short narrative prompt.

Requires OPENAI_API_KEY in the environment for calls.
"""
import os
from typing import Optional

try:
    import openai
except Exception:
    openai = None  # tests/CI can still import the module without a key


def _ensure_openai():
    if openai is None:
        raise RuntimeError("openai package not available. Install via requirements.txt")
    key = os.getenv("OPENAI_API_KEY")
    if not key:
        raise RuntimeError("OPENAI_API_KEY not set in environment")
    openai.api_key = key


def generate_with_openai(prompt: str, model: str = "gpt-3.5-turbo", max_tokens: int = 150, temperature: float = 0.9) -> str:
    """Call OpenAI ChatCompletion and return the assistant text."""
    _ensure_openai()
    resp = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a concise, poetic narrator."},
            {"role": "user", "content": prompt},
        ],
        max_tokens=max_tokens,
        temperature=temperature,
    )
    return resp.choices[0].message.content.strip()


def narrative_from_state(state, model: str = "gpt-3.5-turbo") -> str:
    """Construct a short prompt from the XembraState and return a narrative line."""
    prompt = (
        f"Given an agent state with drift={state.drift:.3f}, entropy={state.entropy:.3f}, "
        f"coherence={state.coherence:.3f}, dream_residue={state.dream_residue:.3f}, "
        "produce one short poetic narrative line (max ~30 words)."
    )
    return generate_with_openai(prompt, model=model, max_tokens=60, temperature=0.9)
