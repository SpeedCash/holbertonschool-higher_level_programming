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
        return self.width  # or self.height, since width == height for Square

    @size.setter
    def size(self, value):
        """Sets the size of the square.
        
        Args:
            value (int): The new size of the square.
            
        Raises:
            TypeError: If 'value' is not an integer.
            ValueError: If 'value' is less than or equal to 0.
        """
        # Utilise les validateurs de la classe Rectangle pour width et height
        self.width = value
        self.height = value

    def __str__(self):
        """Returns the formatted string representation of the Square."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
