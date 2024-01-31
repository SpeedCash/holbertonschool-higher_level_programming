#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):

    for key in sorted(a_dictionary.keys()):
        print(f"{key}: {a_dictionary[key]}")


if __name__ == "__main__":
    a_dictionary = {
        'id': 89,
        'name': "John",
        'age': 23,
        'projects': [1, 2, 3]
    }
    print_sorted_dictionary(a_dictionary)
