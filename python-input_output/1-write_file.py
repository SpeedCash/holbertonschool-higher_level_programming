#!/usr/bin/python3


def write_file(filename="", text=""):
    """Écrit une chaîne dans un fichier texte (UTF-8) et retourne le nombre de
    caractères écrits. Crée le fichier s'il n'existe pas, écrase s'il existe.

    Args:
        filename (str): Nom du fichier à écrire.
        text (str): Texte à écrire dans le fichier.

    Returns:
        int: Nombre de caractères écrits.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
