import argparse
from module_occupation import extract_data, process_data, generate_html

"""
Module principal du projet

.. module:: occupation
   :platform: Unix
   :synopsis: Script principal pour traiter les fichiers ICS et générer un fichier HTML.

.. moduleauthor::  William <>   Charles <>

"""

def main():
    """
    Script principal pour traiter les fichiers ICS et générer un fichier HTML.

    Utilise argparse pour analyser les arguments en ligne de commande et appelle les fonctions
    correspondantes pour extraire les données, les traiter et générer un fichier HTML.

    :return: Aucun retour direct, mais génère un fichier HTML en sortie.
    :rtype: None
    """

    # Ici on utilise le module argparse pour créer des arguments et on leur ajoute une aide (--help/-h)
    parser = argparse.ArgumentParser(description="Ce programme extrait les données d'occupation des salles à partir de fichiers iCalendar (ICS) pour générer un rapport HTML.")
    parser.add_argument("--input-file", nargs="+", help="On indique en argument les trois fichiers ICS")
    parser.add_argument("--output-dir", help="On indique ici le répertoire où le fichier HTML sera créé")
    args = parser.parse_args()

    # On vérifie avec une assertion que la liste des fichiers entrés est bien une liste, et que le chemin relatif des fichiers et du dossier est une chaîne
    assert isinstance(args.input_file, list)
    assert all(isinstance(file_path, str) for file_path in args.input_file)
    assert isinstance(args.output_dir, str)
    
    # Avec la fonction d'extraction de données, on met le contenu des trois fichiers dans la variable de données (data)
    data = extract_data(args.input_file)

    # Avec la fonction de traitement de données, on va découper les événements du calendrier et mettre les éléments importants dans des variables
    processed_data = process_data(data)

    # On génère maintenant la page HTML avec les données traitées
    generate_html(processed_data, args.output_dir)

if __name__ == "__main__":
    main()
