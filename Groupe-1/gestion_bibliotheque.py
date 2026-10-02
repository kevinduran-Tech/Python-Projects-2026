# -*- coding: utf-8 -*-
"""
====================================================================
PROJET 1 : GESTION D'UNE BIBLIOTHÈQUE PERSONNELLE (MANGAS & LIVRES)
Membres du groupe : KAGHO MARIE EDGARD & ADAMOU
====================================================================
"""

import sys

# Configuration sécurisée de l'encodage console pour Windows
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

# Collection initiale contenant les mangas et classiques populaires
bibliotheque = [
    # Mangas classiques
    {"titre": "One Piece", "auteur": "Eiichiro Oda", "annee": 1997, "categorie": "Shonen (aventure)",
     "editeur_jp": "Shueisha", "editeur_fr": "Glenat"},
    {"titre": "Naruto", "auteur": "Masashi Kishimoto", "annee": 1999, "categorie": "Shonen (action, ninja)",
     "editeur_jp": "Shueisha", "editeur_fr": "Kana"},
    {"titre": "Dragon Ball", "auteur": "Akira Toriyama", "annee": 1984, "categorie": "Shonen (aventure, arts martiaux)",
     "editeur_jp": "Shueisha", "editeur_fr": "Glenat"},
    {"titre": "L'Attaque des Titans", "auteur": "Hajime Isayama", "annee": 2009, "categorie": "Shonen (dark fantasy)",
     "editeur_jp": "Kodansha", "editeur_fr": "Pika"},
    {"titre": "Death Note", "auteur": "Tsugumi Oba / Takeshi Obata", "annee": 2003,
     "categorie": "Shonen (thriller psychologique)", "editeur_jp": "Shueisha", "editeur_fr": "Kana"},
    {"titre": "Fullmetal Alchemist", "auteur": "Hiromu Arakawa", "annee": 2001,
     "categorie": "Shonen (fantasy, aventure)", "editeur_jp": "Square Enix", "editeur_fr": "Kurokawa"},
    {"titre": "Demon Slayer", "auteur": "Koyoharu Gotoge", "annee": 2016, "categorie": "Shonen (action, fantasy)",
     "editeur_jp": "Shueisha", "editeur_fr": "Panini"},
    {"titre": "My Hero Academia", "auteur": "Kohei Horikoshi", "annee": 2014, "categorie": "Shonen (super-heros)",
     "editeur_jp": "Shueisha", "editeur_fr": "Ki-oon"},
    {"titre": "Bleach", "auteur": "Tite Kubo", "annee": 2001, "categorie": "Shonen (action, surnaturel)",
     "editeur_jp": "Shueisha", "editeur_fr": "Glenat"},
    {"titre": "Hunter x Hunter", "auteur": "Yoshihiro Togashi", "annee": 1998,
     "categorie": "Shonen (aventure, fantasy)", "editeur_jp": "Shueisha", "editeur_fr": "Kana"},
    {"titre": "Jujutsu Kaisen", "auteur": "Gege Akutami", "annee": 2018, "categorie": "Shonen (dark fantasy, action)",
     "editeur_jp": "Shueisha", "editeur_fr": "Ki-oon"},
    {"titre": "One-Punch Man", "auteur": "ONE / Yusuke Murata", "annee": 2012, "categorie": "Seinen (action, parodie)",
     "editeur_jp": "Shueisha", "editeur_fr": "Kurokawa"},
    {"titre": "Berserk", "auteur": "Kentaro Miura", "annee": 1989, "categorie": "Seinen (dark fantasy)",
     "editeur_jp": "Hakusensha", "editeur_fr": "Glenat"},
    {"titre": "Chainsaw Man", "auteur": "Tatsuki Fujimoto", "annee": 2018, "categorie": "Shonen (action, gore)",
     "editeur_jp": "Shueisha", "editeur_fr": "Kaze / Crunchyroll"},
    {"titre": "Tokyo Ghoul", "auteur": "Sui Ishida", "annee": 2011, "categorie": "Seinen (dark fantasy, horreur)",
     "editeur_jp": "Shueisha", "editeur_fr": "Glenat"}
]


# --- FONCTIONS REQUISES ---

def afficher_livres(liste_livres):
    """Affiche l'ensemble des mangas/livres d'une liste avec mise en forme claire."""
    if not liste_livres:
        print("\n[!] Aucun livre/manga trouve dans la liste.")
        return

    print("\n" + "="*72)
    print(f"{'N°':<4} | {'TITRE':<25} | {'AUTEUR':<20} | {'ANNEE':<6} | {'CATEGORIE'}")
    print("-" * 72)
    for i, m in enumerate(liste_livres, 1):
        titre = (m['titre'][:23] + '..') if len(m['titre']) > 25 else m['titre']
        auteur = (m['auteur'][:18] + '..') if len(m['auteur']) > 20 else m['auteur']
        print(f"{i:<4} | {titre:<25} | {auteur:<20} | {m['annee']:<6} | {m['categorie']}")
        if 'editeur_jp' in m and 'editeur_fr' in m:
            print(f"     └─ Editeur JP: {m['editeur_jp']} | Editeur FR: {m['editeur_fr']}")
    print("=" * 72)


def rechercher_livres():
    """Recherche des livres/mangas selon un critere choisi (titre, auteur, categorie, etc.)."""
    print("\n--- RECHERCHE DE LIVRES / MANGAS ---")
    print("1. Rechercher par Titre")
    print("2. Rechercher par Auteur")
    print("3. Rechercher par Genre / Categorie")
    print("4. Rechercher par Editeur Francais")
    choix = input("Choisissez un critere (1-4) : ").strip()

    cle = ""
    if choix == "1":
        cle = "titre"
    elif choix == "2":
        cle = "auteur"
    elif choix == "3":
        cle = "categorie"
    elif choix == "4":
        cle = "editeur_fr"
    else:
        print("[!] Critere invalide. Retour au menu.")
        return

    valeur_recherche = input(f"Entrez le mot-cle a rechercher pour [{cle}] : ").strip().lower()
    resultats = []

    # Parcours sequentiel avec boucles et conditions
    for manga in bibliotheque:
        valeur_champ = str(manga.get(cle, "")).lower()
        if valeur_recherche in valeur_champ:
            resultats.append(manga)

    print(f"\n[+] {len(resultats)} resultat(s) correspondant a votre recherche.")
    afficher_livres(resultats)


def ajouter_livre():
    """Ajoute un nouvel ouvrage a la collection personnelle."""
    print("\n--- AJOUT D'UN NOUVEAU LIVRE / MANGA ---")
    titre = input("Titre de l'ouvrage : ").strip()
    while not titre:
        titre = input("Le titre ne peut etre vide. Titre : ").strip()

    auteur = input("Auteur : ").strip()
    while not auteur:
        auteur = input("L'auteur ne peut etre vide. Auteur : ").strip()

    while True:
        try:
            annee = int(input("Annee de publication / parution : "))
            if 1000 <= annee <= 2030:
                break
            print("Veuillez saisir une annee realiste (ex: 2005).")
        except ValueError:
            print("[!] Erreur : veuillez entrer une annee valide (nombre entier).")

    categorie = input("Genre / Categorie (ex: Shonen, Roman, Informatique) : ").strip()
    editeur_jp = input("Editeur original / JP (optionnel) : ").strip() or "N/A"
    editeur_fr = input("Editeur francais / distributeur : ").strip() or "N/A"

    nouveau_livre = {
        "titre": titre,
        "auteur": auteur,
        "annee": annee,
        "categorie": categorie,
        "editeur_jp": editeur_jp,
        "editeur_fr": editeur_fr
    }

    bibliotheque.append(nouveau_livre)
    print(f"\n[OK] L'ouvrage '{titre}' a bien ete ajoute a la bibliotheque !")


def modifier_livre():
    """Modifie les informations d'un ouvrage existant."""
    print("\n--- MODIFICATION D'UN LIVRE / MANGA ---")
    afficher_livres(bibliotheque)

    if not bibliotheque:
        return

    try:
        index = int(input("\nEntrez le numero de l'ouvrage a modifier : ")) - 1
        if 0 <= index < len(bibliotheque):
            m = bibliotheque[index]
            print(f"\nModification de : '{m['titre']}' (Appuyez sur Entree pour conserver la valeur actuelle)")

            nouveau_titre = input(f"Titre [{m['titre']}] : ").strip()
            if nouveau_titre:
                m['titre'] = nouveau_titre

            nouvel_auteur = input(f"Auteur [{m['auteur']}] : ").strip()
            if nouvel_auteur:
                m['auteur'] = nouvel_auteur

            annee_str = input(f"Annee [{m['annee']}] : ").strip()
            if annee_str:
                try:
                    m['annee'] = int(annee_str)
                except ValueError:
                    print("Annee invalide, l'ancienne valeur est conservee.")

            nouvelle_cat = input(f"Genre / Categorie [{m['categorie']}] : ").strip()
            if nouvelle_cat:
                m['categorie'] = nouvelle_cat

            nouveau_ed_jp = input(f"Editeur JP [{m.get('editeur_jp', 'N/A')}] : ").strip()
            if nouveau_ed_jp:
                m['editeur_jp'] = nouveau_ed_jp

            nouveau_ed_fr = input(f"Editeur FR [{m.get('editeur_fr', 'N/A')}] : ").strip()
            if nouveau_ed_fr:
                m['editeur_fr'] = nouveau_ed_fr

            print("\n[OK] L'ouvrage a ete mis a jour avec succes.")
        else:
            print("[!] Numero d'index invalide.")
    except ValueError:
        print("[!] Saisie incorrecte. Veuillez entrer un nombre valide.")


def supprimer_livre():
    """Supprime un ouvrage de la collection avec confirmation."""
    print("\n--- SUPPRESSION D'UN LIVRE / MANGA ---")
    afficher_livres(bibliotheque)

    if not bibliotheque:
        return

    try:
        index = int(input("\nEntrez le numero de l'ouvrage a supprimer : ")) - 1
        if 0 <= index < len(bibliotheque):
            manga = bibliotheque[index]
            confirmation = input(f"Etes-vous sur de vouloir supprimer '{manga['titre']}' ? (o/n) : ").lower().strip()
            if confirmation == 'o':
                supprime = bibliotheque.pop(index)
                print(f"\n[OK] L'ouvrage '{supprime['titre']}' a ete retire de la collection.")
            else:
                print("\n[!] Suppression annulee.")
        else:
            print("[!] Numero invalide.")
    except ValueError:
        print("[!] Saisie invalide.")


def afficher_statistiques():
    """Affiche des statistiques descriptives et des rapports analytiques."""
    print("\n--- STATISTIQUES & RAPPORTS DE LA BIBLIOTHEQUE ---")
    total = len(bibliotheque)
    print(f"-> Nombre total d'ouvrages enregistres : {total}")

    if total == 0:
        return

    # Annee min et max
    annees = [m['annee'] for m in bibliotheque if isinstance(m.get('annee'), int)]
    if annees:
        print(f"-> Periode de parution couverte : de {min(annees)} a {max(annees)}")

    # Repartition par categorie
    categories = {}
    for m in bibliotheque:
        cat = m.get('categorie', 'Non specifiee')
        categories[cat] = categories.get(cat, 0) + 1

    print("\n[+] Repartition par categorie :")
    for cat, count in categories.items():
        print(f"    - {cat} : {count} livre(s)")

    # Liste des editeurs
    editeurs = sorted(list(set(m.get('editeur_fr', 'N/A') for m in bibliotheque)))
    print(f"\n[+] Editeurs francais disponibles ({len(editeurs)}) :")
    print(f"    {', '.join(editeurs)}")

    # Rapport filtre par editeur ou categorie
    filtre_ed = input("\nFiltrer la liste par un editeur FR specifique (ou Entree pour ignorer) : ").strip()
    if filtre_ed:
        resultats_ed = [m for m in bibliotheque if m.get('editeur_fr', '').lower() == filtre_ed.lower()]
        print(f"\n--- Titres publies chez '{filtre_ed}' ({len(resultats_ed)}) ---")
        if resultats_ed:
            for item in resultats_ed:
                print(f"  * {item['titre']} - {item['auteur']} ({item['annee']})")
        else:
            print("  Aucun titre trouve pour cet editeur.")


# --- MENU INTERACTIF PRINCIPAL ---

def menu_principal():
    """Point d'entree du programme avec boucle d'interaction utilisateur."""
    while True:
        print("\n" + "="*45)
        print("     GESTION DE BIBLIOTHEQUE PERSONNELLE    ")
        print("          The ICT University - 2026        ")
        print("="*45)
        print("  1. Consulter tous les ouvrages")
        print("  2. Rechercher un ouvrage (multi-criteres)")
        print("  3. Ajouter un nouvel ouvrage")
        print("  4. Modifier un ouvrage existant")
        print("  5. Supprimer un ouvrage")
        print("  6. Consulter les statistiques et rapports")
        print("  7. Quitter le programme")
        print("="*45)

        choix = input("Choisissez une option (1-7) : ").strip()

        if choix == "1":
            afficher_livres(bibliotheque)
        elif choix == "2":
            rechercher_livres()
        elif choix == "3":
            ajouter_livre()
        elif choix == "4":
            modifier_livre()
        elif choix == "5":
            supprimer_livre()
        elif choix == "6":
            afficher_statistiques()
        elif choix == "7":
            print("\nMerci d'avoir utilise le gestionnaire de bibliotheque. Bonne lecture !")
            break
        else:
            print("\n[!] Choix non reconnu. Veuillez saisir un chiffre entre 1 et 7.")


if __name__ == "__main__":
    menu_principal()
