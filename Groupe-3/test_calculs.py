"""Tests simples. Lancer avec : python test_calculs.py"""

from etudiants import ajouter_etudiant, ajouter_note, trouver_etudiant, supprimer_etudiant
from calculs import (
    moyenne_etudiant, moyenne_classe, note_maximale, note_minimale,
    separer_admis_echec, classement,
)


def preparer():
    etudiants = []
    for nom, prenom, notes in [
        ("Nkou", "paul", [12, 14]),      # moyenne 13
        ("Mbarga", "Awa", [8, 9]),       # moyenne 8.5
        ("Tchoua", "Eric", [16, 18]),    # moyenne 17
        ("Fotso", "Lea", []),            # aucune note
    ]:
        ajouter_etudiant(etudiants, nom, prenom)
        for note in notes:
            ajouter_note(trouver_etudiant(etudiants, nom, prenom), note)
    return etudiants


def test_ajout_et_doublon():
    etudiants = preparer()
    assert len(etudiants) == 4
    assert ajouter_etudiant(etudiants, "NKOU", "Paul") is False   # doublon
    assert ajouter_etudiant(etudiants, "", "Paul") is False       # nom vide


def test_note_invalide():
    etudiants = preparer()
    paul = trouver_etudiant(etudiants, "Nkou", "Paul")
    assert ajouter_note(paul, 25) is False
    assert ajouter_note(paul, -1) is False


def test_moyennes():
    etudiants = preparer()
    assert moyenne_etudiant(trouver_etudiant(etudiants, "Nkou", "Paul")) == 13
    assert moyenne_etudiant(trouver_etudiant(etudiants, "Fotso", "Lea")) is None
    assert abs(moyenne_classe(etudiants) - (13 + 8.5 + 17) / 3) < 1e-9


def test_min_max():
    etudiants = preparer()
    assert note_maximale(etudiants) == 18
    assert note_minimale(etudiants) == 8


def test_admis_echec():
    admis, echec = separer_admis_echec(preparer(), 10)
    assert [e["nom"] for e in admis] == ["NKOU", "TCHOUA"]
    assert [e["nom"] for e in echec] == ["MBARGA"]


def test_classement():
    noms = [e["nom"] for e in classement(preparer())]
    assert noms == ["TCHOUA", "NKOU", "MBARGA"]


def test_suppression():
    etudiants = preparer()
    assert supprimer_etudiant(etudiants, "Mbarga", "Awa") is True
    assert supprimer_etudiant(etudiants, "Mbarga", "Awa") is False


if __name__ == "__main__":
    for nom, fonction in list(globals().items()):
        if nom.startswith("test_"):
            fonction()
            print(f"OK  {nom}")
    print("Tous les tests sont passés.")
