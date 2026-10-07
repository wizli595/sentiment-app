#!/usr/bin/env bash
# Mise en place du poste : venv, dépendances, lock, diagnostic.
set -euo pipefail
cd "$(dirname "$0")/.."

PY=$(command -v python3.11 || command -v python3 || command -v python)
[ -d .venv ] || "$PY" -m venv .venv
source .venv/bin/activate 2>/dev/null || source .venv/Scripts/activate

echo "[1/4] Mise à jour de pip"
python -m pip install --upgrade pip --quiet

echo "[2/4] Installation des dépendances (5 à 10 minutes la première fois)"
python -m pip install -r requirements.txt

echo "[3/4] Génération de requirements.lock"
python -m pip freeze > requirements.lock

echo "[4/4] Diagnostic"
python scripts/check_setup.py
