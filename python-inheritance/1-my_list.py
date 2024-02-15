#!/usr/bin/python3

"""
Ce module définit la classe MyList qui hérite de la classe intégrée list.
La classe MyList étend les fonctionnalités de la classe\
    list standard en ajoutant
la méthode print_sorted. Cette méthode permet d'afficher\
    les éléments de la liste
dans un ordre croissant sans modifier la liste originale.
"""


class MyList(list):
    """Hérite de list et ajoute la capacité d'imprimer la liste
    dans un ordre trié."""

    def print_sorted(self):
        """Imprime la liste dans un ordre croissant sans modifier
        la liste originale."""
        print(sorted(self))


if __name__ == "__main__":
    # Exemple de test pour vérifier le fonctionnement de la classe
    my_list = MyList()
    my_list.append(1)
    my_list.append(4)
    my_list.append(2)
    my_list.append(3)
    my_list.append(5)
    print("Liste originale :", my_list)
    print("Liste triée :")
    my_list.print_sorted()
    print("Liste originale après tri :", my_list)
