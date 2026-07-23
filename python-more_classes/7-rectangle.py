#!/usr/bin/python3
"""Module that defines a Rectangle class with a print_symbol attribute."""


class Rectangle:
    """Represent a rectangle.

    This class defines a rectangle by its width and height, both
    stored as private instance attributes accessed through property
    getters/setters. It also provides methods to compute the area
    and the perimeter of the rectangle, to print it using the symbol
    stored in print_symbol, to return an evaluable string
    representation, to print a message when an instance is deleted,
    and it keeps track of how many instances currently exist.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width: The width of the rectangle. Defaults to 0.
            height: The height of the rectangle. Defaults to 0.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than 0.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

        If either width or height is 0, the perimeter is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return the rectangle printed with the print_symbol.

        If either width or height is 0, an empty string is returned.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        rows = [
            str(self.print_symbol) * self.__width
            for _ in range(self.__height)
        ]
        return "\n".join(rows)

    def __repr__(self):
        """Return a string representation to recreate the rectangle."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Print a message when an instance of Rectangle is deleted."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
