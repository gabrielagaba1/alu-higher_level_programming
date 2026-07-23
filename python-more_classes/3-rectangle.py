#!/usr/bin/python3
"""Module that defines a Rectangle class with a string representation."""


class Rectangle:
    """Represent a rectangle.

    This class defines a rectangle by its width and height, which
    are stored as private instance attributes. Access to both is
    controlled through property getters and setters that validate
    the type and value of the assigned data. The class also
    provides methods to compute the area and perimeter, and a
    string representation that draws the rectangle using '#'.
    """

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width: The width of the rectangle. Defaults to 0.
            height: The height of the rectangle. Defaults to 0.
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """Retrieve the current width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle after validation.

        Args:
            value: The new width of the rectangle.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the current height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle after validation.

        Args:
            value: The new height of the rectangle.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the current area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Return the current perimeter of the rectangle.

        If either the width or the height is 0, the perimeter is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """Return the rectangle drawn with the '#' character.

        If either the width or the height is 0, an empty string
        is returned instead.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        rows = ["#" * self.__width for _ in range(self.__height)]
        return "\n".join(rows)
