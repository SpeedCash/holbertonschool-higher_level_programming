#!/usr/bin/python3

def no_c(my_string):

    return ''.join(char for char in my_string if char not in ['c', 'C'])


if __name__ == "__main__":
    chaine = "Concise Code in Python"
    print(no_c(chaine))
