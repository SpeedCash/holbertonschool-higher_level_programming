#!/usr/bin/python3
"""
This module defines a Rectangle class.
The class provides property setters and getters for width and height,
methods to calculate the area and perimeter,
and overrides the __str__, __repr__, and __del__ methods\
    for string representation,
to detect instance deletion, and to keep track of the number of instances.
"""


class Rectangle:
    """Represents a rectangle."""

    # Public class attribute initialized to 0
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initializes the rectangle instance\
            and increments number_of_instances."""
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
        """Returns the printable representation of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(["#" * self.__width for _ in range(self.__height)])

    def __repr__(self):
        """Returns a string representation of the rectangle."""
        return "Rectangle({0}, {1})".format(self.__width, self.__height)

    def __del__(self):
        """Prints a message when an instance of Rectangle is deleted\
            and decrements number_of_instances."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
