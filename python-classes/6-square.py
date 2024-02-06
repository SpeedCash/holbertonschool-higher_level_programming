#!/usr/bin/python3
"""
This module defines a class Square that models a geometric square with
properties such as size and position, and methods to calculate its area and
display it on the console.
"""

class Square:
    """
    A Square class that defines a square by its size and position, offering
    functionalities to calculate its area and print its representation using
    the '#' character.
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a new Square instance with optional size and position.
        
        Args:
            size (int): The size of the square's side. Defaults to 0.
            position (tuple): The square's position as a tuple of 2 positive integers.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Retrieve the size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square, including validation checks.
        
        Args:
            value (int): The new size of the square's side.
        
        Raises:
            TypeError: If the size is not an integer.
            ValueError: If the size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Retrieve the position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set the position of the square, including validation checks.
        
        Args:
            value (tuple): The new position of the square.
        
        Raises:
            TypeError: If the position is not a tuple of 2 positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2 \
           or not all(isinstance(num, int) and num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculate the area of the square.
        
        Returns:
            The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Print the square with the '#' character to the stdout.
        Takes into account the position of the square.
        """
        if self.__size == 0:
            print()
            return
        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
