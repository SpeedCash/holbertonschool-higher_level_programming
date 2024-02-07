#!/usr/bin/python3

class Square:
    """Classe Square qui définit un carré avec une taille spécifique.

    Attributs:
        __size (int): La taille du carré, un détail privé.
    """

    def __init__(self, size):
        """Initialise une nouvelle instance de Square.

        Args:
            size (int): La taille du carré.
        """
        self.__size = size
