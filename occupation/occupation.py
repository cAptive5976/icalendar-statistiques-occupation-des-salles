import module_occupation
import datetime
import argparse

def genere_page_web(nom_fichier, titre_page, corps):
    f = open(nom_fichier,'w',encoding='utf-8')
    HTML_INDEX = """<!DOCTYPE html>
   <html xmlns=\"http://www.w3.org/1999/xhtml\" xml:lang=\"fr\" lang=\"fr\" dir=\"ltr\">
   <head>
   <title>{}</title>
   <style>
      table, th, td {{
      border:1px solid black;
      }}
   </style>
   </head>
   <body>
   {}
   </body>
   </html>
   """.format(titre_page, corps)
    f.write(HTML_INDEX)
    f.close
    

def main():
    corps = """ <h1> Titre </h1>
            """
    genere_page_web("../html/index.html", "mon titre", corps)

if __name__ == "__main__":
    main()
