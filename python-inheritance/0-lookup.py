#!/usr/bin/python3
"""Module that defines a function to list an object's attributes."""


def lookup(obj):
    """Return the list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        A list of strings, one for each attribute or method name.
    """
    return dir(obj)
