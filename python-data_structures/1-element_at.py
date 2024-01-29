#!/usr/bin/python3

def element_at(my_list, idx):

    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]


if __name__ == "__main__":
    ma_liste = [1, 2, 3, 4, 5]
    print(element_at(ma_liste, 2))
    print(element_at(ma_liste, 5))
    print(element_at(ma_liste, -1))
