#!/usr/bin/python3
"""
Module 3-square
Defines a class Square with a private instance attribute size and
a public instance method that returns the square area
"""


class Square:
    """Defines a square by its size, with validation"""
    def __init__(self, size=0):
        """
        Initializes the square

        Args:
        size (int, optional): The size of a side of the square. Defaults to 0.

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
        """Returns the current square area"""
        return self.__size ** 2


if __name__ == "__main__":
    Square = __import__('3-square').Square

    my_square_1 = Square(3)
    print("Area: {}".format(my_square_1.area()))

    try:
        print(my_square_1.size)
    except Exception as e:
        print(e)

    try:
        print(my_square_1.__size)
    except Exception as e:
        print(e)

    my_square_2 = Square(5)
    print("Area: {}".format(my_square_2.area()))
