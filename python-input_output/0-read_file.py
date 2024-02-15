#!/usr/bin/python3
"""
Ce module contient une fonction qui lit et imprime\
    le contenu d'un fichier texte.
"""


def read_file(filename=""):
    """
    Lit un fichier texte en utilisant l'encodage UTF-8 et\
        imprime son contenu à stdout.

    Args:
        filename (str): Le chemin vers le fichier à lire.
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")


if __name__ == "__main__":
    # Test de la fonction
    read_file("my_file_0.txt")
