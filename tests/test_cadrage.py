"""12 tests de cadrage : 4 contrôles sur chacune des 3 fiches."""
import re

import pytest

FICHES = ["cas1-pharmacie.md", "cas2-reglement.md", "cas3-avis-negatifs.md"]

REQUIRED_SECTIONS = [
    "Besoin en une phrase",
    "Utilisateur final",
    "Approche retenue",
    "Justification",
    "Données nécessaires et leur origine",
    "Métrique de succès et seuil d'acceptation",
    "Conséquence d'une erreur et validation humaine prévue",
    "Risques éthiques ou de confidentialité",
]

CRITERIA = ["(a)", "(b)", "(c)", "(d)"]
MIN_BODY_LENGTH = 20
# « Approche retenue » ne contient que des cases à cocher : elle est vérifiée
# par test_exactly_one_approach_checked, pas par la longueur du texte.
CHECKBOX_ONLY_SECTIONS = {"Approche retenue"}


def _section_body(text: str, title: str) -> str | None:
    pattern = re.compile(
        rf"^## {re.escape(title)}.*?$\n(.*?)(?=^## |\Z)", re.M | re.S
    )
    match = pattern.search(text)
    if match is None:
        return None
    body = match.group(1)
    # On retire les lignes de consigne (>) et les lignes de cases à cocher
    kept = [
        line for line in body.splitlines()
        if not line.strip().startswith(">")
        and not line.strip().startswith("- [")
        and line.strip() != "Cocher une seule case :"
    ]
    return "\n".join(kept).strip()


def _read(cadrage_dir, fiche):
    path = cadrage_dir / fiche
    if not path.is_file():
        pytest.fail(f"fiche manquante : {fiche}")
    return path.read_text(encoding="utf-8")


@pytest.mark.parametrize("fiche", FICHES)
def test_fiche_exists(cadrage_dir, fiche):
    assert (cadrage_dir / fiche).is_file(), f"fiche manquante : docs/cadrage/{fiche}"


@pytest.mark.parametrize("fiche", FICHES)
def test_sections_present_and_filled(cadrage_dir, fiche):
    text = _read(cadrage_dir, fiche)
    problems = []
    for title in REQUIRED_SECTIONS:
        body = _section_body(text, title)
        if body is None:
            problems.append(f"rubrique absente : {fiche} / {title}")
        elif title in CHECKBOX_ONLY_SECTIONS:
            continue
        elif len(body) < MIN_BODY_LENGTH:
            problems.append(f"rubriques vides ou trop courtes : {fiche} / {title}")
    assert not problems, " ; ".join(problems)


@pytest.mark.parametrize("fiche", FICHES)
def test_exactly_one_approach_checked(cadrage_dir, fiche):
    text = _read(cadrage_dir, fiche)
    checked = re.findall(r"^- \[x\]", text, re.M | re.I)
    assert len(checked) == 1, (
        f"{fiche} : cocher exactement une approche ({len(checked)} case(s) cochée(s))"
    )


@pytest.mark.parametrize("fiche", FICHES)
def test_justification_cites_criteria(cadrage_dir, fiche):
    text = _read(cadrage_dir, fiche)
    body = _section_body(text, "Justification") or ""
    cited = [c for c in CRITERIA if c in body]
    assert len(cited) >= 2, (
        f"{fiche} : la justification doit citer au moins deux critères "
        f"par leur lettre, trouvés : {cited or 'aucun'}"
    )
