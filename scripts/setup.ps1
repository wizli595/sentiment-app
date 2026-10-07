# Mise en place du poste : venv, dépendances, lock, diagnostic.
$ErrorActionPreference = "Stop"
Set-Location (Join-Path $PSScriptRoot "..")

if (-not (Test-Path ".venv")) {
    $py = Get-Command py -ErrorAction SilentlyContinue
    if ($py) { py -3.11 -m venv .venv } else { python -m venv .venv }
}
& .\.venv\Scripts\Activate.ps1

Write-Host "[1/4] Mise à jour de pip"
python -m pip install --upgrade pip --quiet

Write-Host "[2/4] Installation des dépendances (5 à 10 minutes la première fois)"
python -m pip install -r requirements.txt

Write-Host "[3/4] Génération de requirements.lock"
python -m pip freeze | Out-File -Encoding utf8 requirements.lock

Write-Host "[4/4] Diagnostic"
python scripts\check_setup.py
