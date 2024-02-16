#!/usr/bin/python3
"""
Module 12-pascal_triangle.
Retourne une liste de listes d'entiers représentant le triangle de Pascal
de n niveaux.
"""


def pascal_triangle(n):
    """
    Retourne le triangle de Pascal de n niveaux.

    Paramètres:
    - n (int): Le nombre de niveaux du triangle de Pascal à générer.

    Retourne:
    - Une liste de listes d'entiers représentant le triangle de Pascal.
    Si n <= 0, retourne une liste vide.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)

    return triangle
