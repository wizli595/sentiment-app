"""Diagnostic lisible de l'environnement du TP1.

Cinq blocs : Python, Paquets, Structure du dépôt, Git, Fiches de cadrage.
Trois niveaux : OK (rien à faire), ATTENTION (à corriger avant la fin de
séance), ERREUR (bloquant). Code de sortie 1 s'il reste au moins une erreur.
"""
import importlib
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

MIN_AUTHORS = 2
REQUIRED_DIRS = ["app", "data", "docs", "models", "scripts", "tests", "ui"]
REQUIRED_FILES = ["README.md", "requirements.txt", ".gitignore"]
GITIGNORE_MUST_CONTAIN = [".venv/", "__pycache__/", ".env", "models/", "mlruns/"]
PACKAGES = {"pandas": "pandas", "sklearn": "scikit-learn", "pytest": "pytest"}

errors = 0
warnings = 0


def ok(msg):
    print(f"  OK        {msg}")


def warn(msg):
    global warnings
    warnings += 1
    print(f"  ATTENTION {msg}")


def err(msg):
    global errors
    errors += 1
    print(f"  ERREUR    {msg}")


def check_python():
    print("\n[1/5] Python")
    v = sys.version_info
    if v[:2] == (3, 11):
        ok(f"Python {sys.version.split()[0]}")
    elif v >= (3, 10):
        warn(f"Python {sys.version.split()[0]} : le cours est calé sur 3.11")
    else:
        err(f"Python {sys.version.split()[0]} : 3.10 minimum")
    in_venv = sys.prefix != getattr(sys, "base_prefix", sys.prefix)
    if in_venv:
        ok(f"environnement virtuel actif : {sys.prefix}")
    else:
        err("aucun environnement virtuel actif : activez .venv")


def check_packages():
    print("\n[2/5] Paquets")
    for module, pip_name in PACKAGES.items():
        try:
            importlib.import_module(module)
            ok(f"{pip_name} s'importe")
        except ImportError:
            err(f"{pip_name} absent : python -m pip install {pip_name}")


def check_structure():
    print("\n[3/5] Structure du dépôt")
    for d in REQUIRED_DIRS:
        if (ROOT / d).is_dir():
            ok(f"dossier {d}/")
        else:
            err(f"dossier manquant : {d}/")
    for f in REQUIRED_FILES:
        if (ROOT / f).is_file():
            ok(f"fichier {f}")
        else:
            err(f"fichier manquant : {f}")
    gitignore = ROOT / ".gitignore"
    if gitignore.is_file():
        content = gitignore.read_text(encoding="utf-8")
        missing = [p for p in GITIGNORE_MUST_CONTAIN if p not in content]
        if missing:
            err(f"motifs absents du .gitignore : {', '.join(missing)}")
        else:
            ok("le .gitignore contient les cinq motifs attendus")


def check_git():
    print("\n[4/5] Git")
    if shutil.which("git") is None:
        err("git absent du PATH")
        return
    ok("git est installé")
    if not (ROOT / ".git").exists():
        warn("pas encore de dépôt Git : étape B3")
        return
    ok("dépôt Git initialisé")
    tracked = subprocess.run(
        ["git", "ls-files"], cwd=ROOT, capture_output=True, text=True
    ).stdout.splitlines()
    if any(f.startswith((".venv/", ".venv\\")) for f in tracked):
        err(".venv/ est suivi par Git")
    else:
        ok(".venv/ n'est pas suivi par Git")
    out = subprocess.run(
        ["git", "shortlog", "-sn", "--all"], cwd=ROOT,
        capture_output=True, text=True, encoding="utf-8",
    ).stdout
    authors = [line for line in out.splitlines() if line.strip()]
    if len(authors) >= MIN_AUTHORS:
        ok(f"{len(authors)} auteurs de commits")
    elif authors:
        warn(f"{len(authors)} auteur(s) de commits, {MIN_AUTHORS} attendus")
    else:
        warn("aucun commit : étape B3")


def check_cadrage():
    print("\n[5/5] Fiches de cadrage")
    cadrage = ROOT / "docs" / "cadrage"
    fiches = sorted(cadrage.glob("cas*.md")) if cadrage.is_dir() else []
    if len(fiches) < 3:
        err(f"{len(fiches)} fiche(s) cas*.md trouvée(s), 3 attendues")
        return
    for fiche in fiches:
        text = fiche.read_text(encoding="utf-8")
        checked = re.findall(r"^- \[x\]", text, re.M | re.I)
        if len(checked) == 1:
            ok(f"{fiche.name} : une approche cochée")
        else:
            warn(f"{fiche.name} : {len(checked)} case(s) cochée(s), 1 attendue")


def main():
    print("=== Diagnostic TP1 : sentiment-app ===")
    check_python()
    check_packages()
    check_structure()
    check_git()
    check_cadrage()
    print(f"\nRésumé : {errors} erreur(s), {warnings} avertissement(s)")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
