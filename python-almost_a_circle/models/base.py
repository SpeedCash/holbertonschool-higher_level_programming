#!/usr/bin/python3
"""Module base.py
This module defines the Base class for all other classes in the project.
The Base class aims to manage id attribute in all future classes and to
avoid duplicating the same code.
"""

import json


class Base:
    """A base class for all models.

    Attributes:
        __nb_objects (int): A private class attribute that keeps track of the
                            number of instantiated Bases (if no id is given).
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes a new Base instance.

        Args:
            id (int): The id of the new Base instance. If None, __nb_objects
                      is incremented and used as the new id.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries.

        Args:
            list_dictionaries (list of dict): A list of dictionaries.

        Returns:
            str: The JSON string representation of list_dictionaries.
        """
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)
