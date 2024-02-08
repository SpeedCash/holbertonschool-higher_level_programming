#!/usr/bin/python3
"""
Module 6-square
Defines a class Square with private instance attributes size and position,
with their getters and setters, and methods to calculate\
    its area and print the square.
"""


class Square:
    """Defines a square by its size and position, with validation."""
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes the square

        Args:
        size (int, optional): The size of a side of the square. Defaults to 0.
        position (tuple, optional): The position of the square\
            as a tuple of two integers.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Retrieves the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square, with validation.

        Args:
        value (tuple): The new position of the square.

        Raises:
        TypeError: If position is not a tuple of 2 positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2 \
           or not all(isinstance(num, int) and num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the current square area."""
        return self.size ** 2

    def my_print(self):
        """Prints square with character '#' or an empty line \
        if size is 0, considering its position."""
        if self.size == 0:
            print()
            return
        for _ in range(self.position[1]):
            print()
        for _ in range(self.size):
            print(" " * self.position[0] + "#" * self.size)


if __name__ == "__main__":
    Square = __import__('6-square').Square

    my_square_1 = Square(3)
    my_square_1.my_print()

    print("--")

    my_square_2 = Square(3, (1, 1))
    my_square_2.my_print()

    print("--")

    my_square_3 = Square(3, (3, 0))
    my_square_3.my_print()

    print("--")
