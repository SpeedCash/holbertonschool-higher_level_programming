#!/usr/bin/python3


class Square:
    """Classe Square qui définit un carré avec un attribut privé size."""

    def __init__(self, size):
        """
        Initialise une nouvelle instance de la classe Square.

        Args:
            size (int): La taille du côté du carré.
        """
        self.__size = size
