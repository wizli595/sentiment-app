"""3 tests d'historique Git : commits, auteurs, .venv jamais commité."""
import shutil
import subprocess

import pytest

MIN_AUTHORS = 2


@pytest.fixture(scope="session")
def git_root(root):
    """Saute les tests si Git manque, si .git/ n'existe pas ou sans commit."""
    if shutil.which("git") is None:
        pytest.skip("git absent du PATH")
    if not (root / ".git").exists():
        pytest.skip("pas de dépôt Git : lancez git init (étape B3)")
    probe = subprocess.run(
        ["git", "rev-parse", "HEAD"], cwd=root, capture_output=True, text=True
    )
    if probe.returncode != 0:
        pytest.skip("aucun commit dans le dépôt")
    return root


def _git(git_root, *args) -> str:
    return subprocess.run(
        ["git", *args], cwd=git_root, capture_output=True, text=True,
        encoding="utf-8",
    ).stdout


def test_at_least_one_commit(git_root):
    log = _git(git_root, "log", "--oneline")
    assert log.strip(), "aucun commit dans l'historique"


def test_two_distinct_authors(git_root):
    out = _git(git_root, "shortlog", "-sn", "--all", "HEAD")
    authors = [line for line in out.splitlines() if line.strip()]
    assert len(authors) >= MIN_AUTHORS, (
        f"{len(authors)} auteur(s) de commits, {MIN_AUTHORS} attendus "
        "(un par membre du binôme)"
    )


def test_venv_never_committed(git_root):
    out = _git(git_root, "log", "--all", "--name-only", "--pretty=format:")
    offenders = [
        f for f in out.splitlines()
        if f.startswith(".venv/") or f.startswith(".venv\\")
    ]
    assert not offenders, ".venv/ a été commité au moins une fois dans l'historique"
