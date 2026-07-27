#!/usr/bin/env bash
# Launch XEMBRA app (POSIX)
# Usage: ./scripts/launch.sh
set -euo pipefail

# create venv if missing
if [ ! -d ".venv" ]; then
  python -m venv .venv
fi

# activate
# shellcheck disable=SC1091
. .venv/bin/activate

python -m pip install --upgrade pip
pip install -r requirements.txt

if [ -n "${OPENAI_API_KEY:-}" ]; then
  echo "OPENAI_API_KEY detected. OpenAI backend enabled."
else
  echo "OPENAI_API_KEY not set. Using local backend (gemma) by default."
fi

echo "Starting app.py (press Ctrl+C to stop)..."
python app.py
