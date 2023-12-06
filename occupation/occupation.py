import argparse
from module_occupation import *

def main():
    parser = argparse.ArgumentParser(description="Creation de la bases des deux arguments avec argparse, on l'associe a une variable pour simplfier le code")
    parser.add_argument("--input-file", nargs="+", help="On indique en argument les trois fichiers ICS")
    parser.add_argument("--output-dir", help="On indique ici le repertoire ou le fichier html sera créé")
    args = parser.parse_args()
    data = extract_data(args.input_file)
    processed_data = process_data(data)
    generate_html(processed_data, args.output_dir)

if __name__ == "__main__":
    main()
