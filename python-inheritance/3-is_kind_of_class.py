#!/usr/bin/python3
"""Module that defines a function to check class inheritance."""


def is_kind_of_class(obj, a_class):
    """Check if obj is an instance of a_class or one of its subclasses.

    Args:
        obj: The object to check.
        a_class: The class (or superclass) to compare obj against.

    Returns:
        True if obj is an instance of a_class or a subclass of it,
        otherwise False.
    """
    return isinstance(obj, a_class)
