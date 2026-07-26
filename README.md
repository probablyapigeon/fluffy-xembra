# XEMBRA

A small narrative state-machine engine that models drift, entropy, coherence, and dream residue and emits short narrative lines.

Quickstart

1. Create a venv and install requirements:

   python -m venv .venv
   .venv\\Scripts\\activate
   pip install -r requirements.txt

2. Run the Gradio app:

   python app.py

Files

- modules/xembra_state.py — dataclass holding internal state
- modules/xembra_update.py — state dynamics and update loop
- modules/xembra_narrative.py — narrative generation utilities
- run_engine.py — Engine wrapper (replace with your version if needed)
- app.py — Gradio UI

Initialize a git repo and push (replace URL with your repo):

    git init
    git add .
    git commit -m "Initial commit"
    git branch -M main
    git remote add origin https://github.com/YOURNAME/XEMBRA.git
    git push -u origin main

License: MIT (replace as desired)
