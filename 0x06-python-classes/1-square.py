#!/usr/bin/python3
""" Module """


class Square:
    """ Square class defined
        Attributes:
            size (int): Size of square
            position (tuple): position of space and new lines
    """
    def __init__(self, size=0, position=(0, 0)):
        """initializes
        Args:
            size (int): size
            postion(tuple): postion
        Returns:
            None
        """

        self.size = size
