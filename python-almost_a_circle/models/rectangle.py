#!/usr/bin/python3
"""Module rectangle.py
This module defines the Rectangle class that inherits from Base.
Attributes are protected by using getters and setters for validation.
"""

from models.base import Base


class Rectangle(Base):
    """Defines the Rectangle class that inherits from Base.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.
        __x (int): The x position of the rectangle.
        __y (int): The y position of the rectangle.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a new Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The x position of the rectangle.
            y (int): The y position of the rectangle.
            id (int): The id of the instance.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Gets the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle with validation."""
        self.__width = value

    @property
    def height(self):
        """Gets the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle with validation."""
        self.__height = value

    @property
    def x(self):
        """Gets the x position of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets the x position of the rectangle with validation."""
        self.__x = value

    @property
    def y(self):
        """Gets the y position of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets the y position of the rectangle with validation."""
        self.__y = value
