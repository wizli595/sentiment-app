# Aide-mémoire Git du TP1

## Configuration (une fois par poste)

```bash
git config --global user.name "Prénom Nom"     # ce nom est compté par T5
git config --global user.email "prenom.nom@ecole.ma"
git config --global init.defaultBranch main
```

## Le cycle quotidien

```bash
git pull                        # récupérer le travail de l'autre AVANT de pousser
git status                      # lire ce qui va partir
git add <fichier>               # nommer le fichier, éviter -A après le premier commit
git commit -m "message clair"
git push
```

## Initialiser le dépôt (membre A, une fois)

```bash
git init
git add -A
git status                      # aucune ligne .venv/ — sinon STOP, vérifier .gitignore
git commit -m "Semaine 1 : structure du depot et kit TP1"
git branch -M main
git remote add origin https://github.com/votre-compte/sentiment-app.git
git push -u origin main
```

## Résoudre un conflit sur README.md

`git push` refusé avec `rejected, non-fast-forward` → `git pull`, puis ouvrir
le fichier :

```text
<<<<<<< HEAD
| Membre A | Sara | @sara | |
=======
| Membre B | Omar | @omar | |
>>>>>>> origin/main
```

Garder les deux lignes, supprimer les trois marqueurs, puis :

```bash
git add README.md
git commit
git push
```

Un conflit n'est pas une erreur : Git refuse simplement de choisir à votre place.

## Vérifications

```bash
git shortlog -sn --all          # qui a commité, combien de fois
git log --oneline               # l'historique en une ligne par commit
git ls-files | grep -E "venv|pycache|\.env$|\.zip$"   # doit être vide (sauf .env.example)
```
