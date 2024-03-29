#!/usr/bin/python3
"""
This module defines a Rectangle class with properties width and height,
and public class attributes number_of_instances and print_symbol\
    for string representation.
"""


class Rectangle:
    """Represents a rectangle."""

    number_of_instances = 0  # Public class attribute
    print_symbol = "#"  # Public class attribute, initialized to '#'

    def __init__(self, width=0, height=0):
        """Initializes the rectangle instance."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieves the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Returns the string representation of the rectangle\
            using `print_symbol`."""
        if self.__width == 0 or self.__height == 0:
            return ""
        symbol = str(self.print_symbol)  # Ensures the print_symbol is a string
        return "\n".join([symbol * self.__width for _ in range(self.__height)])

    def __repr__(self):
        """Returns a string representation of the rectangle."""
        return "Rectangle({0}, {1})".format(self.__width, self.__height)

    def __del__(self):
        """Prints a message upon instance deletion and decrements\
            the instance counter."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
