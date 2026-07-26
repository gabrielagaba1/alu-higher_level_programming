#!/usr/bin/python3
"""Module that defines a function to read and print a text file."""


def read_file(filename=""):
    """Read a UTF8 text file and print its contents to stdout.

    Args:
        filename: The path of the file to read.
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
