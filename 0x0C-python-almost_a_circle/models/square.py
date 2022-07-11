#!/usr/bin/python3
"""Module for Square subclass."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """The Square subclass."""
    def __init__(self, size, x=0, y=0, id=None):
        """Constructor"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter - Obtain the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter - Define the size value of this Square."""
        self.width = value
        self.height = value

    def __str__(self):
        """This method returns the str representation of the Square."""
        return "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.x, self.y, self.size)

    def update(self, *args, **kwargs):
        """updates the square attributes taking into account
        the args and kwargs.
        """
        if not args and not kwargs:
            return
        if args:
            content = ["id", "size", "x", "y"]

            for index, worth in enumerate(args):
                if index < len(content):
                    setattr(self, content[index], worth)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """This method returns the dictionary representation of a Square."""
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
