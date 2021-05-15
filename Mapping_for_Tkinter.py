"""
Sylvan Avery Dekker
University of Massachusetts, Amherst
28 June 2019
Project 3
ECE 122
"""

from tkinter import *


class Mapping_for_Tkinter:

    def __init__(self, xmin, xmax, ymin, ymax, width):
        self.__xmin = xmin
        self.__xmax = xmax
        self.__ymin = ymin
        self.__ymax = ymax
        self.__width = width
        self.__height = int(width * ((ymax - ymin) / (xmax - xmin)))

    def set_xmin(self, xmin):
        """
        Set the xmin for the mapping.
        :param xmin: the xmin to set
        """
        self.__xmin = xmin

    def set_xmax(self, xmax):
        """
        Set the xmax for the mapping.
        :param xmax: the xmax to set
        """
        self.__xmax = xmax

    def set_ymin(self, ymin):
        """
        Set the ymin for the mapping.
        :param ymin: the ymin to set
        """
        self.__ymin = ymin

    def set_ymax(self, ymax):
        """
        Set the ymax for the mapping.
        :param ymax: the ymax to set
        """
        self.__ymax = ymax

    def set_width(self, width):
        """
        Set the width for the mapping.
        :param width: the width to set
        """
        self.__width = width

    def __set_height(self, height):
        """
        Set the height for the mapping.
        :param height: the height to set
        """
        self._height = height

    def get_xmin(self):
        """
        Get the xmin of the mapping.
        :return: the xmin used in the mapping
        """
        return self.__xmin

    def get_xmax(self):
        """
        Get the xmax of the mapping.
        :return: the xmax used in the mapping
        """
        return self.__xmax

    def get_ymin(self):
        """
        Get the ymin of the mapping.
        :return: the ymin used in the mapping
        """
        return self.__ymin

    def get_ymax(self):
        """
        Get the ymax of the mapping.
        :return: the ymax used in the mapping
        """
        return self.__ymax

    def get_width(self):
        """
        Get the width of the mapping.
        :return: the width used in the mapping
        """
        return self.__width

    def get_height(self):
        """
        Get the height of the mapping.
        :return: the height used in the mapping
        """
        return self.__height

    def get_x(self, i):
        """
        Map a tkinter i coordinate to an x coordinate in math scale.
        :param i: the tkinter i coordinate
        :return: corresponding x coordinate in math scale
        """
        scale = (self.__xmax - self.__xmin) / (self.__width - 1)
        return scale * i + self.__xmin

    def get_y(self, j):
        """
        Map a tkinter j coordinate to a y coordinate in math scale.
        :param j: the tkinter j coordinate
        :return: corresponding y coordinate in math scale
        """
        scale = (self.__ymin - self.__ymax) / (self.__height - 1)
        return scale * j + self.__ymax

    def get_i(self, x):
        """
        Map a math scale x coordinate to tkinter i coordinate.
        :param x: the y coordinate in math scale
        :return: corresponding j coordinate in tkinter canvas
        """
        return (x - self.__xmin) * (self.__width - 1) // (self.__xmax - self.__xmin)

    def get_j(self, y):
        """
        Map a math scale y coordinate to tkinter j coordinate.
        :param y: the y coordinate in math scale
        :return: corresponding j coordinate in tkinter canvas
        """
        return (y - self.__ymax) * (self.__height - 1) // (self.__ymin - self.__ymax)

    def __str__(self):
        return "Mapping created between x=[%s,%s] y=[%s,%s] math=> (%s,%s) tkinter" %\
               (self.__xmin, self.__xmax, self.__ymin, self.__ymax, self.__width, self.__height)


def main():
    m = Mapping_for_Tkinter(-5.0, 5.0, -5.0, 5.0, 500)  # instantiate mapping
    print(m)  # print info about object

    window = Tk()  # instantiate a tkinter window
    canvas = Canvas(window, width=m.get_width(), height=m.get_height(), bg="white")  # create a canvas width*height
    canvas.pack()

    # create rectangle the Tkinter way
    print("Draw rectangle using tkinter coordinates at (100,400) (400,100)")
    canvas.create_rectangle(100, 400, 400, 100, outline="black")

    # create circle using the mapping
    print("Draw circle using math coordinates at center (0,0) with radius 3")
    canvas.create_oval(m.get_i(-3.0), m.get_j(-3.0), m.get_i(3.0), m.get_j(3.0), outline="blue")

    # create y=x line pixel by pixel using the mapping
    print("Draw line math equation y=x pixel by pixel using the mapping")
    for i in range(m.get_width()):
        x = m.get_x(i)  # obtain the x coordinate
        y = x
        canvas.create_rectangle((m.get_i(x), m.get_j(y))*2, outline="green")

    window.mainloop()  # wait until the window is closed


if __name__ == "__main__":
    main()
