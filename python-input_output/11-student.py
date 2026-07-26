#!/usr/bin/python3
"""Module that defines a Student class with reload_from_json."""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.

        Args:
            first_name: The student's first name.
            last_name: The student's last name.
            age: The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dictionary representation of this Student.

        Args:
            attrs: An optional list of attribute names to include.
                If it's not a list of strings, all attributes are
                retrieved instead.

        Returns:
            A dictionary of this Student's attributes, filtered by
            attrs when applicable.
        """
        if isinstance(attrs, list) and all(
                isinstance(attr, str) for attr in attrs):
            return {
                key: value for key, value in self.__dict__.items()
                if key in attrs
            }
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of this Student from a dictionary.

        Args:
            json: A dictionary mapping attribute names to values.
        """
        for key, value in json.items():
            setattr(self, key, value)
