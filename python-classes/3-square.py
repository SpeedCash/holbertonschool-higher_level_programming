#!/usr/bin/python3

class Square:
    """Classe Square qui définit un carré."""

    def __init__(self, size=0):
        """
        Initialise une nouvelle instance de la classe Square.

        Args:
            size (int): La taille du côté du carré, valeur par défaut de 0.
        Raises:
            TypeError: Si size n'est pas un entier.
            ValueError: Si size est inférieur à 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calcule et retourne l'aire du carré.

        Returns:
            L'aire du carré.
        """
        return self.__size ** 2
