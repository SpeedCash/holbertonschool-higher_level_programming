#!/usr/bin/python3
"""
    hhhhhhhh
"""


class MyList(list):
    """
    MyList étend la classe intégrée list de Python en ajoutant une méthode
    print_sorted, qui affiche la liste dans un ordre croissant sans modifier
    la liste originale.
    """

    def print_sorted(self):
        """
        Imprime les éléments de la liste dans un ordre croissant.
        Cette méthode crée une nouvelle liste triée pour l'affichage,
        laissant la liste originale inchangée.
        """
        print(sorted(self))
