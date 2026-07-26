#!/usr/bin/python3
"""Module that defines a function to write text to a file."""


def write_file(filename="", text=""):
    """Write a string to a UTF8 text file, overwriting it if it exists.

    Args:
        filename: The path of the file to write to.
        text: The string to write to the file.

    Returns:
        The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
