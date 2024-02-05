#!/usr/bin/python3
class Square:
    """Class Square that defines a square by:
    - Private instance attribute: size
    - Instantiation with optional size: def __init__(self, size=0)
    - Property def size(self) to retrieve it
    - Property setter def size(self, value) to set it:
        * size must be an integer, otherwise raise a TypeError exception with the message 'size must be an integer'
        * if size less than 0, raise a ValueError exception with 'size must be >= 0'
    - Public instance method: def area(self) returns current square area.
    """

    def __init__(self, size=0):
        """Initialize the square with an optional size."""
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square, checks integer type and value >= 0."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current square area."""
        return self.__size ** 2
