#!/usr/bin/python3
"""Defines a class-checking function."""


def inherits_from(obj, a_class):
    """Checks if an object is an inherited instance of a class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        If obj is an inherited instance of a_class - True.
        Otherwise - False.
    """
    obj_class = obj.__class__

    while obj_class is not None:
        if obj_class == a_class:
            return False
        obj_class = obj_class.__base__

    return True
