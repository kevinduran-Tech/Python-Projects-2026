#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Projet 3 - Gestion des notes des étudiants
ICT University - Génie Informatique
Cours : Programmation en Python - Année académique 2026-2027

Membres du groupe :
    - NKANO BOLO ULRICH JOEL
    - NAMENI FRANCK JOËL

Description :
    Programme en console permettant de gérer les notes d'un groupe d'étudiants.
    Chaque étudiant est représenté par un dictionnaire {nom, prenom, notes}.
    Tous les étudiants sont stockés dans une liste.
"""

SEUIL_ADMISSION = 10.0   # moyenne minimale pour être admis
NOTE_MIN = 0.0
NOTE_MAX = 20.0

# Liste globale contenant tous les étudiants (chaque étudiant = un dictionnaire)
etudiants = []


# ----------------------------------------------------------------------
# Fonctions utilitaires de saisie
# ----------------------------------------------------------------------
def saisir_note(message):
    """Demande une note valide (entre 0 et 20). Recommence tant que l'entrée est invalide."""
    while True:
        texte = input(message).strip().replace(",", ".")
        try:
            note = float(texte)
        except ValueError:
            print("  Erreur : veuillez entrer un nombre.")
            continue
        if NOTE_MIN <= note <= NOTE_MAX:
            return note
        print(f"  Erreur : la note doit être comprise entre {NOTE_MIN:g} et {NOTE_MAX:g}.")


def saisir_entier(message, minimum, maximum):
    """Demande un entier compris entre minimum et maximum."""
    while True:
        texte = input(message).strip()
        if texte.isdigit() and minimum <= int(texte) <= maximum:
            return int(texte)
        print(f"  Erreur : entrez un entier entre {minimum} et {maximum}.")


def saisir_liste_notes():
    """Saisit une liste de notes ; l'utilisateur tape 'f' pour terminer."""
    notes = []
    print("  Entrez les notes une par une (tapez 'f' pour terminer).")
    while True:
        texte = input(f"  Note {len(notes) + 1} : ").strip().lower()
        if texte == "f":
            break
        texte = texte.replace(",", ".")
        try:
            note = float(texte)
        except ValueError:
            print("  Erreur : nombre invalide.")
            continue
        if NOTE_MIN <= note <= NOTE_MAX:
            notes.append(note)
        else:
            print(f"  Erreur : la note doit être entre {NOTE_MIN:g} et {NOTE_MAX:g}.")
    return notes


def choisir_etudiant():
    """Affiche la liste et retourne l'indice de l'étudiant choisi (ou None)."""
    if not etudiants:
        print("  Aucun étudiant enregistré.")
        return None
    afficher_etudiants()
    numero = saisir_entier("Numéro de l'étudiant : ", 1, len(etudiants))
    return numero - 1


# ----------------------------------------------------------------------
# Gestion des étudiants
# ----------------------------------------------------------------------
def ajouter_etudiant():
    """Ajoute un étudiant (nom, prénom, notes) à la liste."""
    nom = input("Nom : ").strip().upper()
    prenom = input("Prénom : ").strip().title()
    if nom == "" or prenom == "":
        print("  Le nom et le prénom sont obligatoires.")
        return
    notes = saisir_liste_notes()
    etudiants.append({"nom": nom, "prenom": prenom, "notes": notes})
    print(f"  Étudiant {prenom} {nom} ajouté avec succès.")


def saisir_notes():
    """Ajoute de nouvelles notes à un étudiant existant."""
    indice = choisir_etudiant()
    if indice is None:
        return
    etudiant = etudiants[indice]
    etudiant["notes"].extend(saisir_liste_notes())
    print("  Notes enregistrées.")


def modifier_etudiant():
    """Modifie le nom, le prénom ou une note d'un étudiant."""
    indice = choisir_etudiant()
    if indice is None:
        return
    etudiant = etudiants[indice]
    print("  1. Modifier le nom")
    print("  2. Modifier le prénom")
    print("  3. Modifier une note")
    choix = saisir_entier("Votre choix : ", 1, 3)

    if choix == 1:
        etudiant["nom"] = input("Nouveau nom : ").strip().upper()
    elif choix == 2:
        etudiant["prenom"] = input("Nouveau prénom : ").strip().title()
    else:
        if not etudiant["notes"]:
            print("  Cet étudiant n'a aucune note.")
            return
        for i, note in enumerate(etudiant["notes"], start=1):
            print(f"    {i}. {note:g}")
        position = saisir_entier("Numéro de la note à modifier : ", 1, len(etudiant["notes"]))
        etudiant["notes"][position - 1] = saisir_note("Nouvelle valeur : ")
    print("  Modification effectuée.")


def supprimer_etudiant():
    """Supprime un étudiant de la liste après confirmation."""
    indice = choisir_etudiant()
    if indice is None:
        return
    e = etudiants[indice]
    confirmation = input(f"Supprimer {e['prenom']} {e['nom']} ? (o/n) : ").strip().lower()
    if confirmation == "o":
        etudiants.pop(indice)
        print("  Étudiant supprimé.")
    else:
        print("  Suppression annulée.")


# ----------------------------------------------------------------------
# Calculs statistiques
# ----------------------------------------------------------------------
def moyenne_etudiant(etudiant):
    """Retourne la moyenne des notes d'un étudiant (0 s'il n'a pas de notes)."""
    if len(etudiant["notes"]) == 0:
        return 0.0
    total = 0.0
    for note in etudiant["notes"]:
        total += note
    return total / len(etudiant["notes"])


def moyenne_generale():
    """Retourne la moyenne générale de la classe (moyenne des moyennes)."""
    if not etudiants:
        return 0.0
    total = 0.0
    for e in etudiants:
        total += moyenne_etudiant(e)
    return total / len(etudiants)


def note_maximale():
    """Retourne (note, étudiant) de la meilleure note de la classe."""
    meilleure, qui = None, None
    for e in etudiants:
        for note in e["notes"]:
            if meilleure is None or note > meilleure:
                meilleure, qui = note, e
    return meilleure, qui


def note_minimale():
    """Retourne (note, étudiant) de la plus basse note de la classe."""
    plus_basse, qui = None, None
    for e in etudiants:
        for note in e["notes"]:
            if plus_basse is None or note < plus_basse:
                plus_basse, qui = note, e
    return plus_basse, qui


def est_admis(etudiant):
    """Un étudiant est admis si sa moyenne atteint le seuil défini."""
    return etudiant["notes"] != [] and moyenne_etudiant(etudiant) >= SEUIL_ADMISSION


# ----------------------------------------------------------------------
# Tri (tri à bulles : tri simple, du meilleur au moins bon)
# ----------------------------------------------------------------------
def trier_par_moyenne(liste):
    """Retourne une copie de la liste triée par moyenne décroissante (tri à bulles)."""
    copie = liste[:]
    n = len(copie)
    for i in range(n - 1):
        echange = False
        for j in range(n - 1 - i):
            if moyenne_etudiant(copie[j]) < moyenne_etudiant(copie[j + 1]):
                copie[j], copie[j + 1] = copie[j + 1], copie[j]
                echange = True
        if not echange:
            break
    return copie


# ----------------------------------------------------------------------
# Affichages
# ----------------------------------------------------------------------
def afficher_etudiants():
    """Affiche la liste des étudiants avec leurs notes et leur moyenne."""
    if not etudiants:
        print("  Aucun étudiant enregistré.")
        return
    print("\n  N°  Nom / Prénom                    Notes                      Moyenne")
    print("  " + "-" * 75)
    for i, e in enumerate(etudiants, start=1):
        identite = f"{e['nom']} {e['prenom']}"
        notes = ", ".join(f"{n:g}" for n in e["notes"]) or "-"
        print(f"  {i:<3} {identite:<30}  {notes:<25}  {moyenne_etudiant(e):6.2f}")


def afficher_statistiques():
    """Affiche moyenne générale, note maximale et note minimale."""
    if not etudiants:
        print("  Aucun étudiant enregistré.")
        return
    print(f"\n  Moyenne générale de la classe : {moyenne_generale():.2f} / 20")
    maxi, qui_max = note_maximale()
    mini, qui_min = note_minimale()
    if maxi is None:
        print("  Aucune note enregistrée.")
        return
    print(f"  Note maximale : {maxi:g} ({qui_max['prenom']} {qui_max['nom']})")
    print(f"  Note minimale : {mini:g} ({qui_min['prenom']} {qui_min['nom']})")


def afficher_resultats():
    """Affiche les étudiants admis et en échec selon le seuil défini."""
    if not etudiants:
        print("  Aucun étudiant enregistré.")
        return
    print(f"\n  Seuil d'admission : {SEUIL_ADMISSION:g}/20")
    admis, echecs = [], []
    for e in etudiants:
        if est_admis(e):
            admis.append(e)
        else:
            echecs.append(e)
    print(f"\n  ADMIS ({len(admis)}) :")
    for e in admis:
        print(f"    - {e['nom']} {e['prenom']} : {moyenne_etudiant(e):.2f}")
    print(f"\n  EN ÉCHEC ({len(echecs)}) :")
    for e in echecs:
        print(f"    - {e['nom']} {e['prenom']} : {moyenne_etudiant(e):.2f}")


def afficher_classement():
    """Affiche le classement des étudiants par moyenne décroissante."""
    if not etudiants:
        print("  Aucun étudiant enregistré.")
        return
    print("\n  CLASSEMENT DES ÉTUDIANTS")
    print("  " + "-" * 45)
    for rang, e in enumerate(trier_par_moyenne(etudiants), start=1):
        statut = "Admis" if est_admis(e) else "Échec"
        print(f"  {rang:>2}. {e['nom']} {e['prenom']:<15} {moyenne_etudiant(e):6.2f}  {statut}")


# ----------------------------------------------------------------------
# Menu interactif
# ----------------------------------------------------------------------
def afficher_menu():
    print("\n" + "=" * 45)
    print("   GESTION DES NOTES DES ÉTUDIANTS")
    print("=" * 45)
    print(" 1. Ajouter un étudiant")
    print(" 2. Saisir des notes")
    print(" 3. Modifier un étudiant")
    print(" 4. Supprimer un étudiant")
    print(" 5. Afficher les étudiants et leurs moyennes")
    print(" 6. Statistiques (moyenne générale, max, min)")
    print(" 7. Résultats (admis / échec)")
    print(" 8. Classement des étudiants")
    print(" 0. Quitter")
    print("=" * 45)


def main():
    actions = {
        1: ajouter_etudiant,
        2: saisir_notes,
        3: modifier_etudiant,
        4: supprimer_etudiant,
        5: afficher_etudiants,
        6: afficher_statistiques,
        7: afficher_resultats,
        8: afficher_classement,
    }
    while True:
        afficher_menu()
        choix = saisir_entier("Votre choix : ", 0, 8)
        if choix == 0:
            print("Au revoir !")
            break
        actions[choix]()


if __name__ == "__main__":
    main()
