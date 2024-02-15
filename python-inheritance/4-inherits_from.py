#!/usr/bin/python3
"""
    hhhhhhhh
"""


def inherits_from(obj, a_class):
    """Check if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to check against.

    Returns:
        bool: True if obj is an instance of a class that inherited from
        a_class, otherwise False. It returns False if obj is an instance of
        a_class itself.
    """
    return isinstance(obj, a_class) and type(obj) != a_class
