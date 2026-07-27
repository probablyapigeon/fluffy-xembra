# XEMBRA

A small narrative state-machine engine that models drift, entropy, coherence, and dream residue and emits short narrative lines.

Quickstart

1. Create a venv and install requirements:

   python -m venv .venv
   .venv\\Scripts\\activate
   pip install -r requirements.txt

2. Run the Gradio app:

   python app.py

Scripts

- scripts/launch.ps1 — PowerShell helper to create/activate venv, install deps, and run app

Files

- modules/xembra_state.py — dataclass holding internal state
- modules/xembra_update.py — state dynamics and update loop
- modules/xembra_narrative.py — narrative generation utilities
- modules/xembra_adapter.py — pluggable adapter (gemma/openai)
- modules/xembra_llm.py — optional OpenAI integration
- modules/run_engine.py — modules-level Engine export
- run_engine.py — top-level Engine implementation
- app.py — Gradio UI

Secrets

To enable OpenAI backend, add OPENAI_API_KEY as a repository secret (GitHub Settings → Secrets → Actions) or set it in your local shell:

   $env:OPENAI_API_KEY = 'sk-...'

License: MIT (replace as desired)
