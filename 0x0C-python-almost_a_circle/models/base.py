#!/usr/bin/python3
"""Contains a class `Base`"""
import json


class Base:
    """
        Defines the class `Base`
        Attributes:
            id (int): instance attribute
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
            Initializes class and object data
            Args:
                id (int): integer passed on object creation
        """
        self.id = 0
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Converts dictionaries to their string
        representation i.e JSON
        """
        if list_dictionaries is None:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod

