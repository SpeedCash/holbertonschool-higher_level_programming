#!/usr/bin/python3
"""
Module for matrix division. It includes a function that divides all elements
of a matrix by a divisor, checking for the correct types and formats.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div, rounding to 2 decimal places.

    Parameters:
    - matrix: list of lists of int/float, the matrix to divide
    - div: int/float, the divisor

    Returns:
    A new matrix with divided elements, rounded to 2 decimal places.

    Raises:
    - TypeError: For invalid matrix or div types
    - ZeroDivisionError: If div is 0
    """
    if (not all(isinstance(row, list) for row in matrix) or not matrix or
       not all(all(isinstance(elem, (int, float)) for elem in row)
               for row in matrix)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/"
                        "floats")

    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(elem / div, 2) for elem in row] for row in matrix]
