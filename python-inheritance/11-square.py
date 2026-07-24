#!/usr/bin/python3
"""Module that defines a Square class with its own __str__."""
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
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """Return the square description as [Square] w/h."""
        width = self._Rectangle__width
        height = self._Rectangle__height
        return "[Square] {}/{}".format(width, height)
