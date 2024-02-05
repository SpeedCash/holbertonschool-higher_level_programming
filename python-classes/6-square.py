#!/usr/bin/python3


class Square:
    """Class Square that defines a square by:
    - A private instance attribute: size
    - A private instance attribute: position
    - Instantiation with optional size and position
    - Property and property setter for size and position with validation
    - A method to calculate the area of the square
    - A method to print the square using the character '#' considering the position
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square with a default size of 0 and a default position of (0,0), with validation."""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Retrieve the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square with validation."""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current square area."""
        return self.__size ** 2

    def my_print(self):
        """Print the square with the character '#' considering the position."""
        if self.__size == 0:
            print()
            return

        # Print leading spaces for the vertical position
        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            # Print leading spaces for the horizontal position
            print(" " * self.__position[0] + "#" * self.__size)
