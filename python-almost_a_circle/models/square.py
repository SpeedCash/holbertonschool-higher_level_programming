#!/usr/bin/python3
"""Module square.py
Defines the Square class that inherits from Rectangle.
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines the Square class that inherits from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a new Square instance.

        Args:
            size (int): The size of the square.
            x (int): The x position of the square.
            y (int): The y position of the square.
            id (int): The id of the square.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns the formatted string representation of the Square."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """Gets the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Sets the size of the square, adjusting width and height."""
        self.width = value
        self.height = value
