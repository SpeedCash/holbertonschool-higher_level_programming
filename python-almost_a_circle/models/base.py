#!/usr/bin/python3
"""Module base.py
This module defines the Base class for the project 'Almost a Circle'.
The Base class serves as a foundation for all other classes, managing
the id attribute to avoid code duplication.
"""


class Base:
    """Defines the Base class.
    
    Attributes:
        __nb_objects (int): A private class attribute to track the number
                            of objects and to assign new ids.
    """
    
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes a new Base instance.

        Args:
            id (int): The id of the instance. If id is None, __nb_objects
                      is incremented and assigned as the id.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
