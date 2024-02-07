#!/usr/bin/python3
"""
This module defines a function print_square that prints a square with
the character #. The size of the square is determined by the parameter size.
"""


def print_square(size):
    """
    Prints a square with the character #.

    Parameters:
    size (int): The size length of the square.

    Raises:
    TypeError: If size is not an integer or size is a float and is less than 0.
    ValueError: If size is less than 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
