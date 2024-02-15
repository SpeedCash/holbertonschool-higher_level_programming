#!/usr/bin/python3
"""
    hhhhhhhh
"""


class BaseGeometry:
    """BaseGeometry class with validator."""

    def area(self):
        """Not yet implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate value as a positive integer."""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """Rectangle that inherits from BaseGeometry."""

    def __init__(self, width, height):
        """Initialize a new Rectangle."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Return the area of the Rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return the rectangle description."""
        return f"[Rectangle] {self.__width}/{self.__height}"


class Square(Rectangle):
    """Square that inherits from Rectangle."""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size (int): The size of the square.
        """
        super().__init__(size, size)  # Call the Rectangle initialization
        self.__size = size  # Size is both width and height for a square

    def area(self):
        """Return the area of the Square."""
        return self.__size * self.__size
