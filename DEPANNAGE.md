# Dépannage : chercher votre message ici

| Message ou symptôme | Cause | Correction |
| --- | --- | --- |
| `pytest n'est pas reconnu` | Venv non activé | Activer, ou `python -m pytest` |
| `ModuleNotFoundError: No module named 'pandas'` | Venv non activé, ou pip d'un autre Python | `where python` doit contenir `.venv` |
| `test_virtualenv_active` échoue | pytest lancé hors du venv | `.venv\Scripts\python.exe -m pytest` |
| `Activate.ps1 cannot be loaded` | Politique PowerShell | `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` |
| `python` ouvre le Microsoft Store | Alias d'exécution Windows | Paramètres → Applications → Alias d'exécution : désactiver `python.exe` |
| `No matching distribution found for scikit-learn==1.5.*` | Python 3.13/3.14 | Installer 3.11 (ou 3.12), supprimer `.venv`, le recréer |
| `git: command not found` | Git absent du PATH | Installer Git, rouvrir le terminal |
| `Please tell me who you are` | Identité Git non configurée | `git config --global user.name` et `user.email` |
| `error: 400` sur l'URL | Chevrons `<...>` restés dans l'adresse | `git remote set-url origin <vraie URL>` |
| `Repository not found` | Dépôt non créé, ou faute de frappe | Créer le dépôt sur GitHub d'abord |
| `Password authentication is not supported` | Authentification | Jeton d'accès personnel (portée `repo`), ou `gh auth login` |
| `403 Forbidden` | Autorisation | Invitation de collaborateur à envoyer puis accepter |
| `rejected, non-fast-forward` | L'autre membre a poussé entre-temps | `git pull`, résoudre, `git push` |
| `Updates were rejected` au premier push | Dépôt GitHub créé avec un README | `git pull --rebase origin main`, puis `git push` |
| `Your local changes would be overwritten: requirements.lock` | Lock régénéré localement | `git restore requirements.lock`, puis `git pull` |
| `1 auteur(s) de commits, 2 attendus` | Un seul a poussé, ou même `user.name` | Identité distincte, puis un vrai commit |
| `rubriques vides ou trop courtes` | Rubrique de fiche vide | Remplir celle qui est nommée |
| `cocher exactement une approche` | Zéro ou deux croix | Une seule `- [x]` par fiche |
| `la justification doit citer au moins deux critères` | Lettres absentes | Écrire `(a)`, `(c)` explicitement |
| `.venv/ a été commité au moins une fois` | `.gitignore` manquant au `git add -A` | Refaire le dépôt : `rm -rf .git`, vérifier `.gitignore`, `git init`, recommit, `git push --force` ; l'autre membre reclone |
| `4 skipped` alors que le dépôt est sur GitHub | pytest lancé hors du dossier du dépôt | Se placer à la racine du dépôt cloné |
| CI rouge, tests verts en local | Fiches non poussées, ou un seul auteur | Lire le journal d'Actions : mêmes noms de tests |
| `pip install` interminable | Paquets volumineux | Laisser tourner ; les trois paquets de B1 suffisent pour tester |
| Accents cassés dans le terminal | Invite cmd en cp1252 | `chcp 65001`, ou utiliser PowerShell |
| Un zip ou un PDF dans `git status` | Fichier déposé dans le dépôt | `git rm --cached "le fichier"` ; `*.zip` est déjà dans `.gitignore` |

## Si rien ne marche

Appeler l'enseignante avec trois éléments : la commande exacte lancée, le
message complet, et la sortie de `python scripts/check_setup.py`.
