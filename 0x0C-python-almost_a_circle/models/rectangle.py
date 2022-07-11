#!/usr/bin/python3
"""Module for Rectangle subclass."""
from models.base import Base


class Rectangle(Base):
    """This subclass inherits from Base class."""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter - Obtain the width of the rectangle."""
        return self.__width

    @property
    def height(self):
        """Getter - Obtain the height of the rectangle."""
        return self.__height

    @property
    def x(self):
        """Getter - Obtain the x value of the rectangle."""
        return self.__x

    @property
    def y(self):
        """Getter - Obtain the y value of the rectangle."""
        return self.__y

    @width.setter
    def width(self, value):
        """Setter - Define the width value of the rectangle."""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Setter - Define the height value of the rectangle."""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """Setter - Define the x value of the rectangle."""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """Setter - Define the y value of the rectangle."""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """This method returns the area of the rectangle."""
        return self.width * self.height

    def display(self):
        """
        This method prints the graphic representation
        of the rectangle using '#'.
        """
        print("\n" * self.y, end="")
        print((" " * self.x + "#" * self.width + '\n') * self.height, end="")

    def __str__(self):
        """This method returns the str representation of the rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}"\
            .format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """This method updates the Rectangle attributes."""
        if not args and not kwargs:
            return
        if args:
            content = ["id", "width", "height", "x", "y"]

            for index, worth in enumerate(args):
                if index < len(content):
                    setattr(self, content[index], worth)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """This method returns the dictionary representation of a Rectangle."""

        return {
            "id": self.id, "width": self.width, "height": self.height,
            "x": self.x,
            "y": self.y,
        }
