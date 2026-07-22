#!/usr/bin/python3
"""Module that defines a Square class with size and position."""


class Square:
    """Represent a square.

    This class defines a square by its size and position, both
    stored as private instance attributes accessed through property
    getters/setters. It also provides a method to compute the area
    and a method to print the square using the '#' character.
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square.

        Args:
            size: The size of the square. Defaults to 0.
            position: The position of the square. Defaults to (0, 0).

        Raises:
            TypeError: If size is not an integer, or if position is
                not a tuple of 2 positive integers.
            ValueError: If size is less than 0.
        """
        self.size = size
        self.position = position

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
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve the current position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square after validation.

        Args:
            value: The new position of the square.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if (type(value) is not tuple or
                len(value) != 2 or
                not all(type(n) is int for n in value) or
                not all(n >= 0 for n in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square using the '#' character.

        If the size is 0, an empty line is printed instead. The
        position offsets the square with blank lines (vertical) and
        leading spaces (horizontal), without trailing spaces.
        """
        if self.__size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()

        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
