#!/usr/bin/python3

class Square:
    """Define a square by its size to calculate its area."""

    def __init__(self, size=0):
        """
        Initialize a new square.

        Args:
            size (int): The size of a side of the square. Default is 0.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            The area of the square.
        """
        return self.__size ** 2
