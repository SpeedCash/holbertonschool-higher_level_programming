#!/usr/bin/python3
"""
This module defines a function add_integer that adds two numbers.
The function ensures that both numbers are either integers or floats,
casting floats to integers before performing the addition.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats.

    Parameters:
    a (int or float): The first number.
    b (int or float, optional): The second number. Defaults to 98.

    Returns:
    int: The sum of a and b after casting them to integers.

    Raises:
    TypeError: If either a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
