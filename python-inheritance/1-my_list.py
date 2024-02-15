#!/usr/bin/python3

"""
Module implémentant la classe MyList, une sous-classe de\
    list offrant une méthode
supplémentaire, print_sorted, pour afficher ses éléments\
    triés sans modification
de la liste originale. Utilisation typique inclut l'ajout d'éléments suivis par
un affichage trié et non trié pour illustrer la persistance\
    de l'ordre original.
"""


class MyList(list):
    """Extension de list avec une méthode pour imprimer la liste triée."""

    def print_sorted(self):
        """Affiche les éléments de la liste en ordre\
            croissant sans modification."""
        print(sorted(self))


if __name__ == "__main__":
    # Démonstration de MyList
    my_list = MyList([1, 4, 2, 3, 5])
    print("Original:", my_list)
    my_list.print_sorted()
    print("Après print_sorted:", my_list)
