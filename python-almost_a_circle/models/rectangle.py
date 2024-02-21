#!/usr/bin/python3
"""Module rectangle.py
Defines the Rectangle class that inherits from Base.
Includes methods for validation, area calculation, string representation,
displaying, updating attributes, and converting to dictionary representation.
"""

from models.base import Base


class Rectangle(Base):
    """Defines the Rectangle class that inherits from Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a new Rectangle instance."""
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
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Gets the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle with validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Gets the x position of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets the x position of the rectangle with validation."""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Gets the y position of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets the y position of the rectangle with validation."""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area of the Rectangle instance."""
        return self.width * self.height

    def display(self):
        """Prints the Rectangle instance using the '#' character,\
        considering x and y."""
        print("\n" * self.y, end="")
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """Returns the formatted string representation of the Rectangle."""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - \
            {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """Updates attributes of the Rectangle using non-keyword\
            and keyword arguments."""
        attributes = ['id', 'width', 'height', 'x', 'y']
        if args and len(args) > 0:
            for attr, value in zip(attributes, args):
                setattr(self, attr, value)
        else:
            for key, value in kwargs.items():
                if key in attributes:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle."""
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
