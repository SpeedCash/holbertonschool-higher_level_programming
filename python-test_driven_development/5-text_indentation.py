#!/usr/bin/python3
"""
This module defines a function text_indentation that prints a text with two
new lines after each of these characters: '.', '?', and ':'.
The function ensures there's no space at the beginning or at the end of each
printed line.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?', and ':'.

    Parameters:
    text (str): The text to print.

    Raises:
    TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        print(text[i], end="")
        if text[i] in ".?:":
            print("\n" * 2, end="")
            while i + 1 < len(text) and text[i + 1] == " ":
                i += 1
        i += 1
