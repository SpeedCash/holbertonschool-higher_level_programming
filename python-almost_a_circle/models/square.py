#!/usr/bin/python3
"""Module square.py
Defines the Square class that inherits from Rectangle.
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines the Square class that inherits from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a new Square instance."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Gets the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Sets the size of the square, adjusting width and height."""
        self.width = value
        self.height = value

    def __str__(self):
        """Returns the formatted string representation of the Square."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    def update(self, *args, **kwargs):
        """Updates attributes of the Square."""
        if args and len(args) > 0:
            attrs = ['id', 'size', 'x', 'y']
            for attr, value in zip(attrs, args):
                setattr(self, attr, value)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)
