# Raccourcis du TP1 (Linux, macOS, Git Bash)
.PHONY: setup check test

setup:
	bash scripts/setup.sh

check:
	python scripts/check_setup.py

test:
	python -m pytest -q
