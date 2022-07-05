#!/usr/bin/python3
"""Module for BaseGeometry class."""


class BaseGeometry:
    """The BaseGeometry class."""
    def area(self):
        """This method verify the area."""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """This method validates value."""
        if not isinstance(value, int):
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
