"""Calculs sur les notes : moyennes, min/max, admis/échec, classement."""

SEUIL_ADMISSION = 10


def moyenne_etudiant(etudiant):
    """Moyenne d'un étudiant, ou None s'il n'a aucune note."""
    notes = etudiant["notes"]
    if len(notes) == 0:
        return None
    return sum(notes) / len(notes)


def moyenne_classe(etudiants):
    """Moyenne générale = moyenne des moyennes des étudiants ayant des notes."""
    moyennes = []
    for etudiant in etudiants:
        moyenne = moyenne_etudiant(etudiant)
        if moyenne is not None:
            moyennes.append(moyenne)
    if len(moyennes) == 0:
        return None
    return sum(moyennes) / len(moyennes)


def _toutes_les_notes(etudiants):
    notes = []
    for etudiant in etudiants:
        notes.extend(etudiant["notes"])
    return notes


def note_maximale(etudiants):
    """Plus haute note de la classe, ou None s'il n'y a aucune note."""
    notes = _toutes_les_notes(etudiants)
    return max(notes) if notes else None


def note_minimale(etudiants):
    """Plus basse note de la classe, ou None s'il n'y a aucune note."""
    notes = _toutes_les_notes(etudiants)
    return min(notes) if notes else None


def est_admis(etudiant, seuil=SEUIL_ADMISSION):
    """Vrai si la moyenne de l'étudiant atteint le seuil."""
    moyenne = moyenne_etudiant(etudiant)
    return moyenne is not None and moyenne >= seuil


def separer_admis_echec(etudiants, seuil=SEUIL_ADMISSION):
    """Retourne (admis, en_echec). Les étudiants sans note sont ignorés."""
    admis = []
    en_echec = []
    for etudiant in etudiants:
        if moyenne_etudiant(etudiant) is None:
            continue
        if est_admis(etudiant, seuil):
            admis.append(etudiant)
        else:
            en_echec.append(etudiant)
    return admis, en_echec


def classement(etudiants):
    """Étudiants ayant des notes, triés du meilleur au moins bon."""
    avec_notes = [e for e in etudiants if moyenne_etudiant(e) is not None]
    return sorted(avec_notes, key=moyenne_etudiant, reverse=True)
