import argparse
from module_occupation import extract_data, process_data, generate_html

def main():
    """
    Script principal pour traiter les fichiers ICS et générer un fichier HTML.

    Utilise argparse pour analyser les arguments en ligne de commande et appelle les fonctions
    correspondantes pour extraire les données, les traiter et générer un fichier HTML.

    :returns: Aucun retour direct, mais génère un fichier HTML en sortie.
    :rtype: None
    """
    parser = argparse.ArgumentParser(description="Création de la base des deux arguments avec argparse, on l'associe à une variable pour simplifier le code")
    parser.add_argument("--input-file", nargs="+", help="On indique en argument les trois fichiers ICS")
    parser.add_argument("--output-dir", help="On indique ici le répertoire où le fichier HTML sera créé")
    args = parser.parse_args()
    assert isinstance(args.input_file, list)
    assert all(isinstance(file_path, str) for file_path in args.input_file)
    assert isinstance(args.output_dir, str)
    data = extract_data(args.input_file)
    processed_data = process_data(data)
    generate_html(processed_data, args.output_dir)

if __name__ == "__main__":
    main()
