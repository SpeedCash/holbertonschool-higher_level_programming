#!/usr/bin/python3

def uniq_add(my_list=[]):

    unique_elements = set(my_list)

    total = sum(unique_elements)
    return total


if __name__ == "__main__":
    my_list = [1, 2, 3, 2, 4, 3, 2, 1]
    result = uniq_add(my_list)
    print("Sum of unique integers:", result)
