#!/usr/bin/python3

def max_integer(my_list=[]):

    if not my_list:
        return None

    max_val = my_list[0]
    for num in my_list:
        if num > max_val:
            max_val = num

    return max_val


if __name__ == "__main__":
    liste = [1, 2, 3, 4, 5]
    print(max_integer(liste))

    liste_vide = []
    print(max_integer(liste_vide))
