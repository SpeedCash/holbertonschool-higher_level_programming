#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):

    tuple_a += (0, 0)
    tuple_b += (0, 0)

    return tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]


if __name__ == "__main__":
    tuple1 = (1, 2)
    tuple2 = (3, 4)
    print(add_tuple(tuple1, tuple2))

    tuple3 = (1, )
    tuple4 = (3, 4, 5)
    print(add_tuple(tuple3, tuple4))
