# Projet SAE105 Traiter des Données - Occupation des Salles

L’objectif principal de cette SAÉ est d'être confronté à une problématique professionnelle que nous serons amenés à rencontrer en tant que technicien R&T. Ce problème devra être résolu à l’aide d’un programme ou d’un ensemble de programmes et sera pour vous l’occasion de réaliser votre premier projet de développement informatique R&T.

## Auteurs

- [Charles  (cAptive5976)](mailto:)
- [William  (WillixDown)](mailto:)

## Description

Ce projet a pour objectif d’extraire les données des fichiers des emplois du temps des 3 formations du département : BUT1, BUT2, BUT3 que vous aurez préalablement extraits du logiciel ADE de l’Université afin de déterminer pour chaque salle des indicateurs d’occupation.

## Fonctionnalités

- Extraction des données à partir des fichiers iCalendar.
- Traitement des données pour obtenir des informations pertinentes.
- Génération d'un fichier HTML présentant l'occupation des salles.

## Utilisation

1. Cloner le dépôt : `git clone https://github.com/cAptive5976/icalandar-statistiques-occupation-des-salles.git`
2. Se rendre dans le dossier du dépôt : `cd icalandar-statistiques-occupation-des-salles`
3. Exécuter le script principal : 
   - Windows `python occupation/occupation.py --input-file fichier1.ics fichier2.ics fichier3.ics --output-dir html/`
   - Linux `python3 occupation/occupation.py --input-file fichier1.ics fichier2.ics fichier3.ics --output-dir html/`

## Structure du Projet

- `occupation.py`: Script principal pour lancer le traitement.
- `module_occupation.py`: Module contenant les fonctions de traitement des fichiers iCalendar.
- `test_occupation.py`: Fichier de tests unitaires pour les fonctions du module.
- `tests/`: Répertoire contenant les scripts de test unitaire.
- `html/` : Répertoire contenant le fichier HTML généré par le script, ainsi que la feuille de style CSS
- `data/` : Emplacement des fichiers calendriers
- `doc-projet/` : Notre diagramme de cas d'utilisation fait avec Umbrelo
  
## Documentation

Dans le dossier docs une documentation générée avec le logiciel Sphinx sera disponible afin de documenter le projet avec également un rappel du cahier des charges du projet

## Prérequis

- Python 3.x
  
---
