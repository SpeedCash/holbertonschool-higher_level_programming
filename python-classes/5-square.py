#!/usr/bin/python3
"""
Module 5-square
Defines a class Square with private instance attribute size getter and setter,
a method calculate area, and a method print the square using the "#" character.
"""


class Square:
    """Defines square by its size, and includes method to print square."""
    def __init__(self, size=0):
        """
        Initializes the square

        Args:
        size (int, optional): The size of a side of the square. Defaults to 0.
        """
        self.size = size  # Uses the setter

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

    def my_print(self):
        """Prints the square with the character '#' or empty line if size 0."""
        if self.size == 0:
            print()
        else:
            for row in range(self.size):
                print("#" * self.size)


if __name__ == "__main__":
    Square = __import__('5-square').Square

    my_square = Square(3)
    my_square.my_print()

    print("--")

    my_square.size = 10
    my_square.my_print()

    print("--")

    my_square.size = 0
    my_square.my_print()

    print("--")
