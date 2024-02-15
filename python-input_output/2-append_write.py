#!/usr/bin/python3


def append_write(filename="", text=""):
    """Ajoute une chaîne de caractères à la fin d'un fichier texte (UTF-8) et
    retourne le nombre de caractères ajoutés. Le fichier est créé s'il n'existe
    pas.

    Args:
        filename (str): Le nom du fichier à modifier.
        text (str): Le texte à ajouter à la fin du fichier.

    Returns:
        int: Le nombre de caractères ajoutés.
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
