#!/usr/bin/python3
"""Module of Base """

import json
import csv
import turtle


class Base:
    """Type class for base for all other classess"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor - Manage id attribute in future classes."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        This method returns the JSON string to a list of
        dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):

        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_dictionaries = [o.to_dictionary() for o in list_objs]
                f.write(Base.to_json_string(list_dictionaries))

    @staticmethod
    def from_json_string(json_string):

        if json_string is None or json_string == '[]':
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        This method creates a "dummy" instance and updates the
        value of the attributes with those of the given dictionary
        and returns a new object with all attributes already set.
        """
        if cls.__name__ == "Rectangle":
            new_instance = cls(5, 5)
        else:
            new_instance = cls(5)
        new_instance.update(**dictionary)
        return new_instance

    @classmethod
    def load_from_file(cls):
        """
        This method determine if the file exist and returns
        a list of instances(objects) with the id.
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as f:
                list_dictionaries = Base.from_json_string(f.read())
                return [cls.create(**dicti) for dicti in list_dictionaries]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """This method save to CSV file."""
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None:
                f.write("")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """This method loads and reads a CSV file."""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dictionaries = csv.DictReader(csvfile,
                                                   fieldnames=fieldnames)
                list_dictionaries = [dict([i, int(j)]for i, j in dicti.items())
                                     for dicti in list_dictionaries]
                return [cls.create(**dicti) for dicti in list_dictionaries]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """This method draws all the Rectangles and Squares."""
         turtle.Screen()
        turtle.bgcolor("#000C23")
        draw = turtle.Turtle()

        for walk in list_rectangles + list_squares:
            r = random.random()
            g = random.random()
            b = random.random()
            draw.color(r, g, b)
            draw.speed(1.5)
            draw.pensize(4.5)
            draw.begin_fill()
            draw.goto(walk.x, walk.y)
            draw.pendown()
            draw.backward(walk.width)
            draw.right(90)
            draw.backward(walk.height)
            draw.right(90)
            draw.backward(walk.width)
            draw.right(90)
            draw.backward(walk.height)
            draw.right(90)
            draw.penup()
            draw.end_fill()

        turtle.exitonclick()
