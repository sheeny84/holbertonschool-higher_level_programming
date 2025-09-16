#!/usr/bin/python3
"""
This is the "Rectangle" class module.

"""


class Rectangle:
    """
    This is the Rectangle class
    """
    number_of_instances = 0
    print_symbol = "#"

    """
    Initialise a new instance of the Rectangle class

    Args:
        width (int): width of the Rectangle
        height (int): height of the Rectangle
    """
    def __init__(self, width=0, height=0):
        Rectangle.number_of_instances += 1
        self.__dict__ = {}
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height

    def __print__(self):
        """
        Print the current rectangle with the character #
        """
        print(self.__str__)

    def __str__(self):
        """
        Return a string of the current rectangle with the character #
        """
        string = ""
        if self.__width == 0 or self.__height == 0:
            return ""
        for i in range(0, self.__height):
            if i == self.__height-1:
                string = string + self.__width * str(self.print_symbol)
            else:
                string = string + self.__width * str(self.print_symbol) + "\n"
        return string

    def __repr__(self):
        """
        Return a string representation of how to
        create a new instance of the current rectangle
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        Delete the current Rectangle
        """
        print("Bye rectangle...")
        del self
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """
        Return the width of the current rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the current rectangles width

        Args:
            width (int): width of the rectangle
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        Return the height of the current rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the current rectangles height

        Args:
            height (int): height of the rectangle
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        Return the area of the current rectangle
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        Return the perimeter of the current rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2*self.__height + 2*self.__width

    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        area_1 = rect_1.area()
        area_2 = rect_2.area()
        if area_1 >= area_2:
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        return Rectangle(size, size)
