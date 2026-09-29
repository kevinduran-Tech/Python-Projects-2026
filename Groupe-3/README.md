# Groupe 3 – Gestion des notes des étudiants

Programme Python en console permettant de gérer les notes d'un groupe d'étudiants.
Projet de programmation Python – session normale Summer 2026.

## Fonctionnalités

- Ajouter, modifier et supprimer un étudiant
- Saisir les notes (validées entre 0 et 20)
- Moyenne de chaque étudiant, moyenne générale, note maximale et minimale
- Liste des admis et des étudiants en échec selon un seuil (10 par défaut, modifiable)
- Classement des étudiants par moyenne
- Menu interactif

## Structure

| Fichier | Rôle |
|---|---|
| `main.py` | Menu interactif et saisies utilisateur |
| `etudiants.py` | Ajout, modification, suppression, notes |
| `calculs.py` | Moyennes, min/max, admis/échec, classement |
| `test_calculs.py` | Tests simples |

Les étudiants sont des dictionnaires `{"nom", "prenom", "notes"}` stockés dans une liste.

## Lancer le programme

Python 3.8 ou plus récent est nécessaire.

```bash
python main.py
```

## Lancer les tests

```bash
python test_calculs.py
```

## Membres du groupe

- Monkam Kevin Duran — ICTU20241801
- Nassourou Ali — ICTU20251264
- Emoune Massoma Éric Joyce — ICTU20251298

Dirigé par : Monsieur Guy Atangana
