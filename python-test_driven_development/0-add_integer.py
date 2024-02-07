#!/usr/bin/python3
"""
Ce module offre une fonction add_integer qui ajoute deux nombres.

La fonction prend deux paramètres, a et b, qui doivent être des entiers
ou des flottants. Si a ou b ne sont pas de ces types, une TypeError est levée.
"""


def add_integer(a, b=98):
    """
    Ajoute deux entiers ou flottants après les avoir convertis en entiers.

    Args:
        a: Le premier nombre, doit être un entier ou un flottant.
        b: Le deuxième nombre, doit être un entier ou un flottant.

    Returns:
        Le résultat de l'addition des deux nombres convertis en entiers.

    Raises:
        TypeError: Si a ou b ne sont pas des entiers ou des flottants.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
