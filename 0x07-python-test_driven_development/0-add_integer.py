#!/usr/bin/python3
"""define function add_integer"""
def add_integer(a, b=98):
    """function that add 2 integer
        and return value"""
    try:
        a = int(a)
    except ValueError:
        raise TypeError("Error: 'a' must be an integer.")
    try:
        b = int(b)
    except ValueError:
        raise TypeError("Error: 'b' must be an integer.")
    return a + b
