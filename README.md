# sentiment-app

Application d'analyse de sentiment d'avis clients en français — fil rouge du
module « Développement et déploiement d'applications intelligentes » (11 semaines).

Le besoin : l'équipe relation client reçoit des milliers d'avis par jour et les
traite dans l'ordre d'arrivée. On veut faire remonter les avis négatifs en tête
de file pour répondre d'abord aux clients mécontents.

## Installation en trois commandes

```powershell
py -3.11 -m venv .venv            # Linux, macOS : python3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1      # Linux, macOS : source .venv/bin/activate
pip install -r requirements.txt
```

Ou en une commande :

```powershell
powershell -ExecutionPolicy Bypass -File scripts\setup.ps1   # Windows
bash scripts/setup.sh                                        # Linux, macOS, Git Bash
```

Vérification :

```bash
python scripts/check_setup.py     # attendu : 0 erreur(s)
python -m pytest -q               # attendu : 38 passed
```

## Structure

| Dossier | Contient | Se remplit |
| --- | --- | --- |
| `data/` | Jeux de données | Semaine 2 |
| `models/` | Modèles entraînés (jamais dans Git) | Semaine 2 |
| `app/` | API FastAPI | Semaine 3 |
| `ui/` | Interface Streamlit | Semaine 5 |
| `tests/` | 38 tests pytest | Dès aujourd'hui |
| `scripts/` | Installation et diagnostic | Fourni |
| `docs/cadrage/` | Fiches de cadrage | TP1, partie A |

## Le binôme

| Rôle | Nom | GitHub | Signature |
| --- | --- | --- | --- |
| Membre A | Abdellah Wizli | @wizli595 | |
| Membre B | *(à compléter par le membre B)* | | |

## Documents du TP1

- `TP1-ENONCE.md` — l'énoncé : objectifs, livrables, grille de notation
- `MARCHE-A-SUIVRE.md` — le pas à pas : huit étapes, huit contrôles T0 à T7
- `TESTS.md` — la démarche de test et les trois états de référence
- `AIDE-GIT.md` — les commandes Git du TP et la résolution d'un conflit
- `DEPANNAGE.md` — les messages d'erreur et leur correction
