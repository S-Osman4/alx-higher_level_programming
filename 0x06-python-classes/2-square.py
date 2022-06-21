#!/usr/bin/python3
""" Module """


class Square:
    """Defines the square"""
    def __init__(self, size=0):
        """Init the square class
        Args:
            size (int): size of square `size`.
        Raises:
            TypeError: The ``size`` size must be an integer.
            ValueError: ``size`` must be >= 0.        
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
