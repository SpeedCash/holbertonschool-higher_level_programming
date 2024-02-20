#!/usr/bin/python3
"""Module rectangle.py
Defines the Rectangle class that inherits from Base. Includes attribute
validation, area calculation, custom string representation, improved display
method, and an update method that accepts both non-keyword and keyword
arguments.
"""

from models.base import Base


class Rectangle(Base):
    """Defines the Rectangle class that inherits from Base.

    Attributes:
        id (int): The id of the Rectangle, inherited from Base.
        width (int): The width of the Rectangle.
        height (int): The height of the Rectangle.
        x (int): The x position of the Rectangle.
        y (int): The y position of the Rectangle.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a new Rectangle instance."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
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
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} \
            - {self.width}/{self.height}"

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
