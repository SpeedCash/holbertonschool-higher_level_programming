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


if __name__ == "__main__":
    # Création d'une instance de MyList
    my_list = MyList()
    my_list.append(1)
    my_list.append(4)
    my_list.append(2)
    my_list.append(3)
    my_list.append(5)

    # Affichage de la liste originale
    print("Liste originale:", my_list)

    # Affichage de la liste triée
    my_list.print_sorted()

    # Confirmation que la liste originale reste inchangée
    print("Liste après print_sorted:", my_list)
