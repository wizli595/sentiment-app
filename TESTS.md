# La démarche de test

Le kit vérifie deux fois les mêmes choses, par deux chemins. `check_setup.py`
parle aux humains (OK, ATTENTION, ERREUR). `pytest` parle aux machines, et
c'est lui que la CI et la notation utilisent.

## Les 38 tests

| Fichier | Tests | Ce qui est vérifié |
| --- | --- | --- |
| `test_environment.py` | 23 | Python ≥ 3.10, venv actif, 3 paquets importables, 7 dossiers, 4 fichiers, versions figées, 5 motifs du `.gitignore`, ni `.env` ni `.venv/` suivis |
| `test_cadrage.py` | 12 | Par fiche : existence, 8 rubriques remplies (≥ 20 caractères hors consigne), exactement un `- [x]`, au moins deux critères cités |
| `test_git_history.py` | 3 | Au moins un commit, au moins 2 auteurs, `.venv/` absent de tout l'historique (skippés tant qu'il n'y a pas de dépôt) |

## Les trois états de référence

| Moment | `python -m pytest -q` |
| --- | --- |
| Kit fraîchement décompressé, venv actif | `3 failed, 31 passed, 4 skipped` |
| Fiches remplies, avant le dépôt Git | `35 passed, 3 skipped` |
| Fin de séance, deux commits poussés | `38 passed` |

Un test rouge avant que le travail soit fait est un test utile ; un test vert
dès le départ ne vérifie rien.

## Les paramètres réglables

| Paramètre | Fichier | Valeur |
| --- | --- | --- |
| `MIN_AUTHORS` | `check_setup.py`, `test_git_history.py` | 2 |
| `REQUIRED_DIRS` | `check_setup.py`, `test_environment.py` | 7 dossiers |
| `GITIGNORE_MUST_CONTAIN` | `check_setup.py`, `test_environment.py` | 5 motifs |
| `REQUIRED_SECTIONS` | `test_cadrage.py` | 8 rubriques |
| `CRITERIA` | `test_cadrage.py` | (a) à (d) |

Ne les modifiez pas pour faire passer un test : c'est exactement ce que la
notation regarde.
