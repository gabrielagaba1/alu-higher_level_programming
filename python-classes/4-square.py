#!/usr/bin/python3
"""Module that defines a Square class with a size property."""


class Square:
    """Represent a square.

    This class defines a square by its size, which is stored as a
    private instance attribute. Access to the size is controlled
    through a property getter and setter, allowing type and value
    validation to be centralized in one place.
    """

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size: The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """Retrieve the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square after validation.

        Args:
            value: The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >=
self.__size = value

    def area(self):
        """Return the current area of the square."""
        return self.__size * self.__size
