#!/usr/bin/python3
"""
This module defines the add_integer function that adds two numbers.
The function is designed to meet the specific requirements and test cases
outlined in the project instructions and the associated test file.
"""


def add_integer(a, b=98):
    """
    Adds two numbers after validating their type.

    Args:
        a (int, float): The first number, must be an integer or float.
        b (int, float, optional): Second number, must be an integer or float.
            Defaults to 98.

    Returns:
        int: The sum of a and b as integers.

    Raises:
        TypeError: If either a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
