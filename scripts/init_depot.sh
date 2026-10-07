#!/usr/bin/env bash
# Initialise le dépôt local et le pousse vers GitHub.
# Refuse de pousser si .venv/ est en attente de commit.
# Usage : bash scripts/init_depot.sh https://github.com/votre-compte/sentiment-app.git
set -euo pipefail
cd "$(dirname "$0")/.."

URL="${1:?Usage : bash scripts/init_depot.sh <URL HTTPS du dépôt GitHub>}"

[ -d .git ] || git init
git add -A

if git status --porcelain | grep -q "\.venv/"; then
    echo "ERREUR : .venv/ est en attente de commit. Vérifiez .gitignore." >&2
    exit 1
fi

git commit -m "Semaine 1 : structure du depot et kit TP1"
git branch -M main
git remote add origin "$URL" 2>/dev/null || git remote set-url origin "$URL"
git push -u origin main
