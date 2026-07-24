#!/usr/bin/python3
"""Module that defines a function to check strict inheritance."""


def inherits_from(obj, a_class):
    """Check if obj's class inherited from a_class.

    Args:
        obj: The object to check.
        a_class: The class to check inheritance from.

    Returns:
        True if obj is an instance of a subclass of a_class (not
        a_class itself), otherwise False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
