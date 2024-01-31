#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):

    a_dictionary.pop(key, None)
    return a_dictionary


if __name__ == "__main__":
    a_dictionary = {'id': 89, 'name': "John", 'age': 23}
    print("Original dictionary:", a_dictionary)

    simple_delete(a_dictionary, 'name')
    print("Dictionary after deleting 'name':", a_dictionary)

    simple_delete(a_dictionary, 'height')
    print("Dictionary after trying to delete 'height':", a_dictionary)
