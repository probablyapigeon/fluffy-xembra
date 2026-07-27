"""Demo script to run XEMBRA with OpenAI backend if OPENAI_API_KEY is set.
Usage:
  OPENAI_API_KEY=sk-... python scripts/demo_openai.py
"""
import os
from modules.run_engine import Engine

if __name__ == "__main__":
    key = os.getenv("OPENAI_API_KEY")
    if not key:
        print("OPENAI_API_KEY not set. Set it in the environment to run OpenAI-backed demo.")
        raise SystemExit(1)

    eng = Engine(backend="openai")
    try:
        line = eng.step()
        print("OpenAI-backed line:\n", line)
    except Exception as e:
        print("OpenAI generation failed:", e)
        print("Falling back to local generator:")
        eng.set_backend("gemma")
        print(eng.step())
