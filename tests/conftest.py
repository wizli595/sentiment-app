"""Fixtures partagées par tous les tests du TP1."""
from pathlib import Path

import pytest


@pytest.fixture(scope="session")
def root() -> Path:
    """Racine du dépôt, calculée une fois par session."""
    return Path(__file__).resolve().parents[1]


@pytest.fixture(scope="session")
def cadrage_dir(root: Path) -> Path:
    """Dossier des fiches de cadrage."""
    return root / "docs" / "cadrage"
