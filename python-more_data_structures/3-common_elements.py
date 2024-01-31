#!/usr/bin/python3

def common_elements(set_1, set_2):

    return set_1 & set_2


if __name__ == "__main__":
    set_1 = {1, 2, 3, 4, 5}
    set_2 = {4, 5, 6, 7, 8}

    common = common_elements(set_1, set_2)
    print("Common elements:", common)
