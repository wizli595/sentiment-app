# Marche à suivre : huit étapes, huit contrôles

Ne passez à l'étape suivante que lorsque le contrôle précédent a donné le
résultat attendu, qu'il soit vert ou, dans deux cas précis (T1, premier passage
CI), rouge.

## Préparation (5 min)

Décompresser le kit, se placer dans `sentiment-app/`, répartir les rôles
(membre A : crée le dépôt GitHub ; membre B : clone une fois créé).

**Contrôle T0** — `ls -Force` montre sept dossiers (`app`, `data`, `docs`,
`models`, `scripts`, `tests`, `ui`), six documents, `requirements.txt`,
`pytest.ini` et `.gitignore`.

## Partie A : cadrage (50 min, à deux)

- **A1 (5 min)** : lire `docs/cadrage/EXEMPLE-corrige.md`.
- **A2 (40 min)** : remplir `cas1-pharmacie.md`, `cas2-reglement.md`,
  `cas3-avis-negatifs.md`. Une seule case cochée, au moins deux critères cités
  par leur lettre, chaque rubrique obligatoire remplie.

**Contrôle T2** — `python -m pytest tests/test_cadrage.py -q` : **12 passed**.

## Partie B : environnement et dépôt (70 min)

### B1. Environnement virtuel (10 min, chacun)

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install pandas scikit-learn pytest
```

**Contrôle T1** — `python -m pytest -q` : **3 failed, 31 passed, 4 skipped**.
Ce rouge est voulu : il décrit le travail de la séance.

### B2. Créer le dépôt GitHub (10 min, membre A)

Private, sans README ni `.gitignore` ; membre B en Write, enseignant en Read.

### B3. Initialiser et pousser (15 min, membre A)

```bash
git init
git add -A
git status          # CONTRÔLE T3 : aucune ligne .venv/ — IRRÉVERSIBLE sinon
git commit -m "Semaine 1 : structure du depot et kit TP1"
git branch -M main
git remote add origin https://github.com/votre-compte/sentiment-app.git
git push -u origin main
```

### B4. Installation complète (15 min, les deux)

Le membre B clone d'abord, puis chacun :

```powershell
powershell -ExecutionPolicy Bypass -File scripts\setup.ps1
```

**Contrôle T4** — `python scripts/check_setup.py` : **0 erreur(s)**.

### B5. Un commit par membre (10 min, chacun)

```bash
git pull
# ajouter sa ligne au tableau du binôme dans README.md
git add README.md
git commit -m "README : ajout de <nom> au tableau du binome"
git push
```

**Contrôle T5** — `git shortlog -sn --all` : deux noms distincts ;
`python -m pytest tests/test_git_history.py -q` : **3 passed**.

### B6. Vérification finale (10 min, à deux)

**Contrôle T6** — `python scripts/check_setup.py` : 0 erreur, 0 avertissement ;
`python -m pytest -q` : **38 passed** ; onglet Actions vert.

### B7. Le test de l'enseignant (5 min)

```bash
bash scripts/verif_clone.sh https://github.com/votre-compte/sentiment-app.git
```

**Contrôle T7** — 0 erreur au diagnostic et 38 passed sur un clone frais, sans
aucune intervention manuelle.
