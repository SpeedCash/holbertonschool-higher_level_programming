#!/usr/bin/python3
"""
This module defines a write_file function that writes a string to a text file
(UTF8) and returns the number of characters written. It demonstrates basic file
handling in Python, including creating or overwriting a file without the need
for importing external modules.
"""


def write_file(filename="", text=""):
    """Write a string to a text file (UTF8) and return the number of characters written.
    
    Args:
        filename (str): The name of the file to write to.
        text (str): The text to write to the file.
        
    Returns:
        int: The number of characters written.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)

if __name__ == "__main__":
    # This block is for demonstration and testing.
    # It will not be executed when importing this script as a module.
    write_file = __import__('1-write_file').write_file

    nb_characters = write_file("my_first_file.txt", "This School is so cool!\n")
    print(nb_characters)
