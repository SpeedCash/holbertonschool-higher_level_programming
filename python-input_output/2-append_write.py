#!/usr/bin/python3
"""
A simple Python module to demonstrate file handling. It includes a function
write_file that writes a specified string to a text file, using UTF-8 encoding.
The function will create the file if it doesn't exist, or overwrite it if it does.
This demonstrates basic file I/O operations, error handling, and the use of
the 'with' statement for efficient and safe handling of file resources.
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
