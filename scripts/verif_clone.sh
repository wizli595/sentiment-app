#!/usr/bin/env bash
# Rejoue le test de l'enseignant : clone frais, installation, diagnostic, tests.
# Usage : bash scripts/verif_clone.sh https://github.com/votre-compte/sentiment-app.git
set -euo pipefail

URL="${1:?Usage : bash scripts/verif_clone.sh <URL HTTPS du dépôt GitHub>}"
TMP=$(mktemp -d)
trap 'rm -rf "$TMP"' EXIT

git clone "$URL" "$TMP/verif"
cd "$TMP/verif"

PY=$(command -v python3.11 || command -v python3 || command -v python)
"$PY" -m venv .venv
source .venv/bin/activate 2>/dev/null || source .venv/Scripts/activate
python -m pip install --upgrade pip --quiet
python -m pip install -r requirements.txt
python scripts/check_setup.py
python -m pytest -q
echo "Clone frais : tout est passé."
