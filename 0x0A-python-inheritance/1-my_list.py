#!/usr/bin/python3
"""MyList class."""


class MyList(list):
    """This class inherits from list."""
    def print_sorted(self):
        print(sorted(self))
        """This method print the sorted list."""
