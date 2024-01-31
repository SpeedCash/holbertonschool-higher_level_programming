#!/usr/bin/python3

def number_keys(a_dictionary):

    return len(a_dictionary)


if __name__ == "__main__":
    a_dictionary = {'id': 89, 'name': "John", 'age': 23, 'projects': [1, 2, 3]}
    print("Number of keys:", number_keys(a_dictionary))
