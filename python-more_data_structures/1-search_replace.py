#!/usr/bin/python3

def search_replace(my_list, search, replace):

    return [replace if x == search else x for x in my_list]


if __name__ == "__main__":
    my_list = [1, 2, 3, 2, 4]
    search = 2
    replace = 99

    new_list = search_replace(my_list, search, replace)
    print("Original list:", my_list)
    print("Modified list:", new_list)
