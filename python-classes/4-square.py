#!/usr/bin/python3
"""
Module 4-square
Defines a class Square with a private instance attribute getter and setter,
and a public instance method that returns the square area
"""


class Square:
    """Defines a square by its size, with validation calculate its area."""
    def __init__(self, size=0):
        """
        Initializes the square

        Args:
        size (int, optional): The size of a side of the square. Defaults to 0.
        """
        self.size = size  # Utilizes the setter to enforce type/value checks

    @property
    def size(self):
        """Retrieves the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square, with validation.

        Args:
        value (int): The new size of the square.

        Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current square area."""
        return self.size ** 2


if __name__ == "__main__":
    Square = __import__('4-square').Square

    my_square = Square(89)
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))

    my_square.size = 3
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))

    try:
        my_square.size = "5 feet"
        print("Area: {} for size: {}".format(my_square.area(), my_square.size))
    except Exception as e:
        print(e)
