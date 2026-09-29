"""Gestion des notes des étudiants – programme principal (menu interactif)."""

from etudiants import (
    NOTE_MIN, NOTE_MAX,
    trouver_etudiant, ajouter_etudiant, ajouter_note, remplacer_notes,
    modifier_etudiant, supprimer_etudiant, afficher_etudiants,
)
from calculs import (
    SEUIL_ADMISSION, moyenne_etudiant, moyenne_classe, note_maximale,
    note_minimale, separer_admis_echec, classement,
)


def lire_note(message):
    """Demande une note valide. Retourne None si l'utilisateur laisse vide."""
    while True:
        saisie = input(message).strip().replace(",", ".")
        if saisie == "":
            return None
        try:
            note = float(saisie)
        except ValueError:
            print("Saisie invalide : entrez un nombre.")
            continue
        if NOTE_MIN <= note <= NOTE_MAX:
            return note
        print(f"La note doit être comprise entre {NOTE_MIN} et {NOTE_MAX}.")


def lire_seuil(message):
    """Demande un seuil valide (nombre entre 0 et 20)."""
    while True:
        saisie = input(message).strip().replace(",", ".")
        try:
            seuil = float(saisie)
        except ValueError:
            print("Saisie invalide : entrez un nombre.")
            continue
        if NOTE_MIN <= seuil <= NOTE_MAX:
            return seuil
        print(f"Le seuil doit être compris entre {NOTE_MIN} et {NOTE_MAX}.")


def choisir_etudiant(etudiants):
    """Demande nom et prénom, retourne l'étudiant ou None s'il n'existe pas."""
    nom = input("Nom : ")
    prenom = input("Prénom : ")
    etudiant = trouver_etudiant(etudiants, nom, prenom)
    if etudiant is None:
        print("Étudiant introuvable.")
    return etudiant


def menu_ajouter(etudiants):
    nom = input("Nom : ")
    prenom = input("Prénom : ")
    if ajouter_etudiant(etudiants, nom, prenom):
        print("Étudiant ajouté.")
    else:
        print("Impossible : nom/prénom vide ou étudiant déjà existant.")


def menu_saisir_notes(etudiants):
    etudiant = choisir_etudiant(etudiants)
    if etudiant is None:
        return
    print("Entrez les notes une par une (laissez vide pour terminer).")
    while True:
        note = lire_note("Note : ")
        if note is None:
            break
        ajouter_note(etudiant, note)
    print("Notes enregistrées.")


def menu_modifier(etudiants):
    etudiant = choisir_etudiant(etudiants)
    if etudiant is None:
        return
    print("1. Modifier le nom et le prénom")
    print("2. Remplacer toutes les notes")
    choix = input("Votre choix : ").strip()
    if choix == "1":
        nom = input("Nouveau nom : ")
        prenom = input("Nouveau prénom : ")
        if modifier_etudiant(etudiants, etudiant, nom, prenom):
            print("Étudiant modifié.")
        else:
            print("Impossible : nom/prénom vide ou déjà utilisé.")
    elif choix == "2":
        nouvelles = []
        print("Entrez les nouvelles notes (laissez vide pour terminer).")
        while True:
            note = lire_note("Note : ")
            if note is None:
                break
            nouvelles.append(note)
        remplacer_notes(etudiant, nouvelles)
        print("Notes remplacées.")
    else:
        print("Choix invalide.")


def menu_supprimer(etudiants):
    nom = input("Nom : ")
    prenom = input("Prénom : ")
    if supprimer_etudiant(etudiants, nom, prenom):
        print("Étudiant supprimé.")
    else:
        print("Étudiant introuvable.")


def menu_statistiques(etudiants):
    moyenne = moyenne_classe(etudiants)
    if moyenne is None:
        print("Aucune note enregistrée.")
        return
    print(f"Moyenne générale de la classe : {moyenne:.2f}")
    print(f"Note maximale : {note_maximale(etudiants):g}")
    print(f"Note minimale : {note_minimale(etudiants):g}")
    print("\nMoyenne par étudiant :")
    for etudiant in etudiants:
        m = moyenne_etudiant(etudiant)
        texte = f"{m:.2f}" if m is not None else "aucune note"
        print(f"  {etudiant['nom']} {etudiant['prenom']} : {texte}")


def menu_admis_echec(etudiants, seuil):
    admis, en_echec = separer_admis_echec(etudiants, seuil)
    print(f"Seuil d'admission : {seuil:g}")
    print(f"\nAdmis ({len(admis)}) :")
    for etudiant in admis:
        print(f"  {etudiant['nom']} {etudiant['prenom']} – {moyenne_etudiant(etudiant):.2f}")
    print(f"\nEn échec ({len(en_echec)}) :")
    for etudiant in en_echec:
        print(f"  {etudiant['nom']} {etudiant['prenom']} – {moyenne_etudiant(etudiant):.2f}")


def menu_classement(etudiants):
    classes = classement(etudiants)
    if len(classes) == 0:
        print("Aucun étudiant avec des notes.")
        return
    print(f"{'Rang':<6}{'Nom':<15}{'Prénom':<15}Moyenne")
    print("-" * 46)
    for rang, etudiant in enumerate(classes, start=1):
        print(f"{rang:<6}{etudiant['nom']:<15}{etudiant['prenom']:<15}"
              f"{moyenne_etudiant(etudiant):.2f}")


def afficher_menu(seuil):
    print("\n===== GESTION DES NOTES =====")
    print("1. Ajouter un étudiant")
    print("2. Saisir des notes")
    print("3. Modifier un étudiant")
    print("4. Supprimer un étudiant")
    print("5. Afficher tous les étudiants")
    print("6. Statistiques de la classe")
    print("7. Admis / en échec")
    print("8. Classement")
    print(f"9. Changer le seuil d'admission (actuel : {seuil:g})")
    print("0. Quitter")


def main():
    etudiants = []
    seuil = SEUIL_ADMISSION
    while True:
        afficher_menu(seuil)
        choix = input("Votre choix : ").strip()
        print()
        if choix == "1":
            menu_ajouter(etudiants)
        elif choix == "2":
            menu_saisir_notes(etudiants)
        elif choix == "3":
            menu_modifier(etudiants)
        elif choix == "4":
            menu_supprimer(etudiants)
        elif choix == "5":
            afficher_etudiants(etudiants)
        elif choix == "6":
            menu_statistiques(etudiants)
        elif choix == "7":
            menu_admis_echec(etudiants, seuil)
        elif choix == "8":
            menu_classement(etudiants)
        elif choix == "9":
            seuil = lire_seuil("Nouveau seuil : ")
        elif choix == "0":
            print("Au revoir !")
            break
        else:
            print("Choix invalide, réessayez.")


if __name__ == "__main__":
    main()
