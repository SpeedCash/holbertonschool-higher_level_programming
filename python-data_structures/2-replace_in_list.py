#!/usr/bin/python3

def replace_in_list(my_list, idx, element):

    if 0 <= idx < len(my_list):
        my_list[idx] = element
    return my_list


if __name__ == "__main__":
    ma_liste = [1, 2, 3, 4, 5]
    print(replace_in_list(ma_liste, 2, 9))
    print(replace_in_list(ma_liste, 5, 8))
    print(replace_in_list(ma_liste, -1, 7))
