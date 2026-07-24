#!/usr/bin/python3
"""Module that defines a Rectangle class with area and __str__."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a rectangle, validated using BaseGeometry."""

    def __init__(self, width, height):
        """Initialize a new Rectangle.

        Args:
            width: The width of the rectangle. Must be a positive
                integer.
            height: The height of the rectangle. Must be a positive
                integer.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than or equal to 0.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return the current area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return the rectangle description as [Rectangle] w/h."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
