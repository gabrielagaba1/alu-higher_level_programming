#!/usr/bin/python3
"""Module that defines a Square class with an area method."""


class Square:
    """Represent a square.

    This class defines a square by its size, which is stored as a
    private instance attribute. The size is validated to ensure it
    is a non-negative integer, and the class provides a method to
    compute the area of the square.
    """

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
size: The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current area of the square."""
        return self.__size * self.__size
