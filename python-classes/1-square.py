#!/usr/bin/python3
"""Module that defines a Square class with a private size attribute."""


class Square:
    """Represent a square.

    This class defines a square by its size, which is stored as a
    private instance attribute and cannot be accessed directly from
    outside the class.
    """

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size: The size of the square. No type or value
                verification is performed on this argument.
        """
        self.__size = size
