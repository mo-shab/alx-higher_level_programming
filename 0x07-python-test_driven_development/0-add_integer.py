#!/usr/bin/python3


"""define function add_integer"""


def add_integer(a, b=98):
    """function that add 2 integer
        and return value"""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b