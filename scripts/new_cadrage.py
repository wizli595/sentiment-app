"""Crée une fiche de cadrage supplémentaire à partir du modèle.

Usage : python scripts/new_cadrage.py cas4-mon-sujet
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = ROOT / "docs" / "cadrage" / "TEMPLATE.md"


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage : python scripts/new_cadrage.py cas4-mon-sujet")
    name = sys.argv[1].removesuffix(".md")
    target = ROOT / "docs" / "cadrage" / f"{name}.md"
    if target.exists():
        sys.exit(f"{target.name} existe déjà")
    target.write_text(TEMPLATE.read_text(encoding="utf-8"), encoding="utf-8")
    print(f"Fiche créée : docs/cadrage/{target.name}")


if __name__ == "__main__":
    main()
