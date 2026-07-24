#!/usr/bin/python3
"""Module that defines a Square class inheriting from Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square, validated using BaseGeometry."""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size: The width and height of the square. Must be a
                positive integer.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than or equal to 0.
        """
        super().__init__(size, size)
