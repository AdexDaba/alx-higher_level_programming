#!/usr/bin/python3
"""
    Module contains of a single class
"""


class Rectangle:
    """Defines a reactangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializing of instance data"""
        if not isinstance(width, (int, float)):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, (int, float)):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """Prints rectangle using `print_symbol` character"""
        string = []
        if self.__width == 0 or self.__height == 0:
            return ""

        if not isinstance(self.print_symbol, str):
            self.print_symbol = str(self.print_symbol)
        for i in range(self.__height):
            for j in range(self.__width):
                string.append(self.print_symbol)
            if i < (self.__height - 1):
                string.append("\n")
        return "".join(string)

    def __repr__(self):
        """Prints string representation of Rectangle"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Prints a string when instane being deleted"""

