#!/usr/bin/python3

def delete_at(my_list=[], idx=0):

    if 0 <= idx < len(my_list):
        return my_list[:idx] + my_list[idx+1:]
    return my_list


if __name__ == "__main__":
    ma_liste = [1, 2, 3, 4, 5]
    print(delete_at(ma_liste, 2))
    print(delete_at(ma_liste, 5))
    print(delete_at(ma_liste, -1))
