# Launch XEMBRA app (PowerShell)
# Usage: Open PowerShell, run: .\scripts\launch.ps1

# Allow running this script only for the current process
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process -Force

# Create and activate venv if missing
if (-Not (Test-Path -Path ".venv\Scripts\Activate.ps1")) {
    python -m venv .venv
}

Write-Host "Activating virtual environment..."
. .venv\Scripts\Activate.ps1

Write-Host "Upgrading pip and installing requirements..."
python -m pip install --upgrade pip
pip install -r requirements.txt

# Optional: set OPENAI_API_KEY in this shell before running to enable OpenAI backend
if ($env:OPENAI_API_KEY) {
    Write-Host "OPENAI_API_KEY detected in environment. OpenAI backend enabled."
} else {
    Write-Host "OPENAI_API_KEY not set. Using local backend (gemma) by default."
}

Write-Host "Starting app.py (press Ctrl+C to stop)..."
python app.py
