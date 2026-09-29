"""Gestion des étudiants : ajout, modification, suppression, saisie des notes.

Chaque étudiant est un dictionnaire :
    {"nom": "NKOU", "prenom": "Paul", "notes": [12.5, 14.0]}
Tous les étudiants sont stockés dans une liste.
"""

NOTE_MIN = 0
NOTE_MAX = 20


def _normaliser(nom, prenom):
    """Retourne (nom en majuscules, prénom avec majuscule initiale)."""
    return nom.strip().upper(), prenom.strip().title()


def trouver_etudiant(etudiants, nom, prenom):
    """Retourne l'étudiant correspondant, ou None s'il n'existe pas."""
    nom, prenom = _normaliser(nom, prenom)
    for etudiant in etudiants:
        if etudiant["nom"] == nom and etudiant["prenom"] == prenom:
            return etudiant
    return None


def ajouter_etudiant(etudiants, nom, prenom):
    """Ajoute un étudiant sans note. Retourne False si vide ou déjà présent."""
    nom, prenom = _normaliser(nom, prenom)
    if nom == "" or prenom == "":
        return False
    if trouver_etudiant(etudiants, nom, prenom) is not None:
        return False
    etudiants.append({"nom": nom, "prenom": prenom, "notes": []})
    return True


def ajouter_note(etudiant, note):
    """Ajoute une note comprise entre 0 et 20. Retourne False si invalide."""
    if not NOTE_MIN <= note <= NOTE_MAX:
        return False
    etudiant["notes"].append(note)
    return True


def remplacer_notes(etudiant, nouvelles_notes):
    """Remplace toutes les notes d'un étudiant (les notes invalides sont ignorées)."""
    etudiant["notes"] = [n for n in nouvelles_notes if NOTE_MIN <= n <= NOTE_MAX]


def modifier_etudiant(etudiants, etudiant, nouveau_nom, nouveau_prenom):
    """Change le nom et le prénom. Retourne False si vide ou déjà utilisé."""
    nouveau_nom, nouveau_prenom = _normaliser(nouveau_nom, nouveau_prenom)
    if nouveau_nom == "" or nouveau_prenom == "":
        return False
    autre = trouver_etudiant(etudiants, nouveau_nom, nouveau_prenom)
    if autre is not None and autre is not etudiant:
        return False
    etudiant["nom"] = nouveau_nom
    etudiant["prenom"] = nouveau_prenom
    return True


def supprimer_etudiant(etudiants, nom, prenom):
    """Supprime un étudiant. Retourne False s'il n'existe pas."""
    etudiant = trouver_etudiant(etudiants, nom, prenom)
    if etudiant is None:
        return False
    etudiants.remove(etudiant)
    return True


def afficher_etudiants(etudiants):
    """Affiche la liste des étudiants avec leurs notes."""
    if len(etudiants) == 0:
        print("Aucun étudiant enregistré.")
        return
    print(f"{'N°':<4}{'Nom':<15}{'Prénom':<15}Notes")
    print("-" * 60)
    for i, etudiant in enumerate(etudiants, start=1):
        notes = ", ".join(f"{n:g}" for n in etudiant["notes"]) or "aucune"
        print(f"{i:<4}{etudiant['nom']:<15}{etudiant['prenom']:<15}{notes}")
