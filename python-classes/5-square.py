#!/usr/bin/python3
class Square:
    """Class Square that defines a square by:
    - A private instance attribute: size
    - Instantiation with optional size: def __init__(self, size=0)
    - Property and property setter to retrieve and set it with validation
    - A method to calculate the area of the square
    - A method to print the square using the character '#'
    """

    def __init__(self, size=0):
        """Initialize the square with a default size of 0, with validation."""
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current square area."""
        return self.__size ** 2

    def my_print(self):
        """Print the square with the character '#'."""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
