# if no .venv folder, create it
if (-not (Test-Path -Path .venv)) {
    python -m venv .venv

# activate the virtual environment
.venv\Scripts\activate.ps1

pip install --upgrade pip
pip install -r requirements.txt
pyinstaller --onefile --windowed gui.py