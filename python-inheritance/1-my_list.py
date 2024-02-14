#!/usr/bin/python3
class MyList(list):
    """Inherits from list and adds the ability to print the list\
        in sorted order."""

    def print_sorted(self):
        """Prints the list in ascending order without altering\
            the original list."""
        print(sorted(self))


if __name__ == "__main__":
    # Exemple de test pour vérifier le fonctionnement de la classe
    my_list = MyList()
    my_list.append(1)
    my_list.append(4)
    my_list.append(2)
    my_list.append(3)
    my_list.append(5)
    print(my_list)
    my_list.print_sorted()
    print(my_list)
