#!/usr/bin/python3
""" Module """



class Square:
    """Defines the square"""
    def __init__(self, size=0):
        """Constructor
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
        else:
            self.__size = size
            
    def area(self):
        """ Calculate the area of a square.
        Return:
        Power of square size.
        """
        
        return ((self.__size) ** 2)
