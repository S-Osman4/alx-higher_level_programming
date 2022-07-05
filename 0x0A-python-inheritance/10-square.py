#!/usr/bin/python3
"""Module for Square subclass."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """The Square subclass."""
    def __init__(self, size):
        """Instantiation with size."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """This method returns the area of the square."""
        return self.__size * self.__size
