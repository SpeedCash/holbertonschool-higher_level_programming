#!/usr/bin/python3

def new_in_list(my_list, idx, element):

    list_copy = my_list[:]
    if 0 <= idx < len(list_copy):
        list_copy[idx] = element
    return list_copy


if __name__ == "__main__":
    ma_liste = [1, 2, 3, 4, 5]
    nouvelle_liste = new_in_list(ma_liste, 2, 9)
    print(nouvelle_liste)
    print(ma_liste)
