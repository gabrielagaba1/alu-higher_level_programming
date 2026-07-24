#!/usr/bin/python3
"""Module that defines a function to check exact class membership."""


def is_same_class(obj, a_class):
    """Check if obj is exactly an instance of a_class.

    Args:
        obj: The object to check.
        a_class: The class to compare obj's type against.

    Returns:
        True if type(obj) is exactly a_class, otherwise False.
    """
    return type(obj) is a_class
