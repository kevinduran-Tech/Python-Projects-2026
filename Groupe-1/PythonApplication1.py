# Collection initiale contenant vos mangas et d'autres classiques populaires
bibliotheque = [
    # Vos 10 mangas
    {"titre": "One Piece", "auteur": "Eiichiro Oda", "annee": 1997, "categorie": "Shōnen (aventure)", "editeur_jp": "Shūeisha", "editeur_fr": "Glénat"},
    {"titre": "Naruto", "auteur": "Masashi Kishimoto", "annee": 1999, "categorie": "Shōnen (action, ninja)", "editeur_jp": "Shūeisha", "editeur_fr": "Kana"},
    {"titre": "Dragon Ball", "auteur": "Akira Toriyama", "annee": 1984, "categorie": "Shōnen (aventure, arts martiaux)", "editeur_jp": "Shūeisha", "editeur_fr": "Glénat"},
    {"titre": "L'Attaque des Titans", "auteur": "Hajime Isayama", "annee": 2009, "categorie": "Shōnen (dark fantasy)", "editeur_jp": "Kōdansha", "editeur_fr": "Pika"},
    {"titre": "Death Note", "auteur": "Tsugumi Ōba / Takeshi Obata", "annee": 2003, "categorie": "Shōnen (thriller psychologique)", "editeur_jp": "Shūeisha", "editeur_fr": "Kana"},
    {"titre": "Fullmetal Alchemist", "auteur": "Hiromu Arakawa", "annee": 2001, "categorie": "Shōnen (fantasy, aventure)", "editeur_jp": "Square Enix", "editeur_fr": "Kurokawa"},
    {"titre": "Demon Slayer", "auteur": "Koyoharu Gotōge", "annee": 2016, "categorie": "Shōnen (action, fantasy)", "editeur_jp": "Shūeisha", "editeur_fr": "Panini"},
    {"titre": "My Hero Academia", "auteur": "Kōhei Horikoshi", "annee": 2014, "categorie": "Shōnen (super-héros)", "editeur_jp": "Shūeisha", "editeur_fr": "Ki-oon"},
    {"titre": "Bleach", "auteur": "Tite Kubo", "annee": 2001, "categorie": "Shōnen (action, surnaturel)", "editeur_jp": "Shūeisha", "editeur_fr": "Glénat"},
    {"titre": "Hunter x Hunter", "auteur": "Yoshihiro Togashi", "annee": 1998, "categorie": "Shōnen (aventure, fantasy)", "editeur_jp": "Shūeisha", "editeur_fr": "Kana"},
    
    # Mangas populaires ajoutés
    {"titre": "Jujutsu Kaisen", "auteur": "Gege Akutami", "annee": 2018, "categorie": "Shōnen (dark fantasy, action)", "editeur_jp": "Shūeisha", "editeur_fr": "Ki-oon"},
    {"titre": "One-Punch Man", "auteur": "ONE / Yusuke Murata", "annee": 2012, "categorie": "Seinen (action, parodie)", "editeur_jp": "Shūeisha", "editeur_fr": "Kurokawa"},
    {"titre": "Berserk", "auteur": "Kentaro Miura", "annee": 1989, "categorie": "Seinen (dark fantasy)", "editeur_jp": "Hakusensha", "editeur_fr": "Glénat"},
    {"titre": "Chainsaw Man", "auteur": "Tatsuki Fujimoto", "annee": 2018, "categorie": "Shōnen (action, gore)", "editeur_jp": "Shūeisha", "editeur_fr": "Kazé / Crunchyroll"},
    {"titre": "Tokyo Ghoul", "auteur": "Sui Ishida", "annee": 2011, "categorie": "Seinen (dark fantasy, horreur)", "editeur_jp": "Shūeisha", "editeur_fr": "Glénat"}
]

# --- FONCTIONS REQUISES ---

def afficher_livres(liste_livres):
    """Affiche l'ensemble des mangas d'une liste."""
    if not liste_livres:
        print("\nAucun manga trouvé.")
        return
    
    print("\n--- LISTE DES MANGAS ---")
    for i, m in enumerate(liste_livres, 1):
        print(f"{i}. [Titre] {m['titre']} | [Auteur] {m['auteur']} | [Année JP] {m['annee']} | [Genre] {m['categorie']}")
        print(f"   └─ Editeur JP: {m['editeur_jp']} | Editeur FR: {m['editeur_fr']}")

def rechercher_livres():
    """Recherche des mangas selon un critère choisi."""
    print("\n--- RECHERCHE DE MANGAS ---")
    print("1. Rechercher par Titre")
    print("2. Rechercher par Auteur")
    print("3. Rechercher par Genre / Catégorie")
    print("4. Rechercher par Éditeur Français")
    choix = input("Choisissez un critère (1-4) : ")
    
    cle = ""
    if choix == "1": cle = "titre"
    elif choix == "2": cle = "auteur"
    elif choix == "3": cle = "categorie"
    elif choix == "4": cle = "editeur_fr"
    else:
        print("Critère invalide.")
        return

    valeur_recherche = input(f"Entrez la valeur à rechercher ({cle}) : ").lower()
    resultats = []
    
    # Boucle et conditions pour le filtrage
    for manga in bibliotheque:
        if valeur_recherche in manga[cle].lower():
            resultats.append(manga)
            
    afficher_livres(resultats)

def ajouter_livre():
    """Ajoute un nouveau manga à la collection."""
    print("\n--- AJOUTER UN MANGA ---")
    titre = input("Titre du manga : ").strip()
    auteur = input("Auteur : ").strip()
    
    while True:
        try:
            annee = int(input("Année de sortie au Japon : "))
            break
        except ValueError:
            print("Veuillez entrer une année valide (nombre entier).")
            
    categorie = input("Genre / Catégorie : ").strip()
    editeur_jp = input("Éditeur japonais : ").strip()
    editeur_fr = input("Éditeur français : ").strip()
    
    nouveau_manga = {
        "titre": titre, "auteur": auteur, "annee": annee,
        "categorie": categorie, "editeur_jp": editeur_jp, "editeur_fr": editeur_fr
    }
    
    bibliotheque.append(nouveau_manga)
    print(f"\nLe manga '{titre}' a bien été ajouté.")

def modifier_livre():
    """Modifie les informations d'un manga existant."""
    print("\n--- MODIFIER UN MANGA ---")
    afficher_livres(bibliotheque)
    
    if not bibliotheque: return
        
    try:
        index = int(input("\nEntrez le numéro du manga à modifier : ")) - 1
        if 0 <= index < len(bibliotheque):
            m = bibliotheque[index]
            print(f"\nModification de : {m['titre']}")
            
            m['titre'] = input(f"Nouveau titre [{m['titre']}] : ").strip() or m['titre']
            m['auteur'] = input(f"Nouvel auteur [{m['auteur']}] : ").strip() or m['auteur']
            
            annee_str = input(f"Nouvelle année [{m['annee']}] : ").strip()
            m['annee'] = int(annee_str) if annee_str else m['annee']
            
            m['categorie'] = input(f"Nouveau genre [{m['categorie']}] : ").strip() or m['categorie']
            m['editeur_jp'] = input(f"Nouvel éditeur JP [{m['editeur_jp']}] : ").strip() or m['editeur_jp']
            m['editeur_fr'] = input(f"Nouvel éditeur FR [{m['editeur_fr']}] : ").strip() or m['editeur_fr']
            
            print("\nManga mis à jour avec succès.")
        else:
            print("Numéro invalide.")
    except ValueError:
        print("Saisie incorrecte.")

def supprimer_livre():
    """Supprime un manga de la collection."""
    print("\n--- SUPPRIMER UN MANGA ---")
    afficher_livres(bibliotheque)
    
    if not bibliotheque: return
        
    try:
        index = int(input("\nEntrez le numéro du manga à supprimer : ")) - 1
        if 0 <= index < len(bibliotheque):
            manga_supprime = bibliotheque.pop(index)
            print(f"\nLe manga '{manga_supprime['titre']}' a été supprimé.")
        else:
            print("Numéro invalide.")
    except ValueError:
        print("Saisie incorrecte.")

def afficher_statistiques():
    """Affiche des rapports simples sur la collection."""
    print("\n--- STATISTIQUES & RAPPORTS ---")
    total = len(bibliotheque)
    print(f"Nombre total de mangas enregistrés : {total}")
    
    if total == 0: return
        
    # Extraction des éditeurs uniques
    editeurs = set(m['editeur_fr'] for m in bibliotheque)
    print(f"Éditeurs français présents : {', '.join(editeurs)}")
    
    choix_editeur = input("\nEntrez un éditeur français pour voir ses mangas (ou Entrée pour ignorer) : ").strip()
    if choix_editeur:
        filtre = [m for m in bibliotheque if m['editeur_fr'].lower() == choix_editeur.lower()]
        print(f"\n--- Mangas édités par '{choix_editeur}' ---")
        if filtre:
            for m in filtre:
                print(f"- {m['titre']} ({m['auteur']})")
        else:
            print("Aucun manga trouvé pour cet éditeur.")

# --- MENU INTERACTIF PRINCIPAL ---

def menu_principal():
    """Boucle principale gérant l'interface utilisateur."""
    while True:
        print("\n=================================")
        print("    MANGA COLLECTION MANAGER     ")
        print("=================================")
        print("1. Consulter tous les mangas")
        print("2. Rechercher un manga")
        print("3. Ajouter un manga")
        print("4. Modifier un manga")
        print("5. Supprimer un manga")
        print("6. Voir les statistiques / rapports")
        print("7. Quitter le programme")
        print("=================================")
        
        choix = input("Choisissez une option (1-7) : ").strip()
        
        if choix == "1": afficher_livres(bibliotheque)
        elif choix == "2": rechercher_livres()
        elif choix == "3": ajouter_livre()
        elif choix == "4": modifier_livre()
        elif choix == "5": supprimer_livre()
        elif choix == "6": afficher_statistiques()
        elif choix == "7":
            print("\nProgramme fermé. Bonne lecture !")
            break
        else:
            print("\nOption invalide, veuillez choisir un nombre entre 1 et 7.")

if __name__ == "__main__":
    menu_principal()
