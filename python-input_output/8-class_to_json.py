#!/usr/bin/python3
"""Module that defines a function to prepare an object for JSON."""


def class_to_json(obj):
    """Return the dictionary description of a simple-attribute object.

    Args:
        obj: An instance of a class whose attributes are all
            serializable (list, dict, str, int, bool).

    Returns:
        A dictionary of obj's instance attributes.
    """
    return obj.__dict__
