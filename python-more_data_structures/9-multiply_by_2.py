#!/usr/bin/python3

def multiply_by_2(a_dictionary):

    return {key: value * 2 for key, value in a_dictionary.items()}


if __name__ == "__main__":
    a_dictionary = {'id': 89, 'score': 10, 'height': 6}
    new_dictionary = multiply_by_2(a_dictionary)
    print("Original dictionary:", a_dictionary)
    print("New dictionary:", new_dictionary)
