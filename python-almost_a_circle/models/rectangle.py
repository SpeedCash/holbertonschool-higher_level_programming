#!/usr/bin/python3
"""Module rectangle.py
Updates the Rectangle class with attribute validation, a method to calculate
its area, and a method to print its representation using '#'.
"""

from models.base import Base


class Rectangle(Base):
    """Defines the Rectangle class that inherits from Base.
    Adds validation to the setter methods to ensure that input values
    meet the required criteria. Includes methods to calculate the area
    of the rectangle and to display the rectangle using the '#' character.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a new Rectangle instance with validation."""
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
        """Prints the Rectangle instance using the '#' character."""
        for _ in range(self.height):
            print("#" * self.width)

    def __str__(self):
        """Returns the formatted string representation of the Rectangle."""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} \
            - {self.width}/{self.height}"

    def display(self):
        """Prints the Rectangle instance using the '#' character,\
        taking care of x and y."""
        print("\n" * self.y, end="")
        for row in range(self.height):
            print(" " * self.x + "#" * self.width)

    def update(self, *args):
        """Updates the Rectangle attributes using no-keyword arguments."""
        attributes = ['id', 'width', 'height', 'x', 'y']
        for attr, value in zip(attributes, args):
            setattr(self, attr, value)
