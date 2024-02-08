#!/usr/bin/python3
"""
Module 1-square
Defines a class Square with a private instance attribute size
"""


class Square:
    """Defines a square by its size

    Attributes:
    size (int): The size of a side of the square
    """
    def __init__(self, size):
        """
        Initializes the square

        Args:
        size (int): The size of a side of square, no type/value verification
        """
        self.__size = size


if __name__ == "__main__":
    Square = __import__('1-square').Square

    my_square = Square(3)
    print(type(my_square))
    print(my_square.__dict__)

    try:
        print(my_square.size)
    except Exception as e:
        print(e)

    try:
        print(my_square.__size)
    except Exception as e:
        print(e)
