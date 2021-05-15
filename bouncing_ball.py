"""
Sylvan Avery Dekker
University of Massachusetts, Amherst
28 June 2019
Project 3
ECE 122
"""

from Mapping_for_Tkinter import Mapping_for_Tkinter
from tkinter import *
import math
import time


class Ball:
    def __init__(self, x0, y0, v, theta, radius):
        self.__x = x0
        self.__y = y0
        self.__v = v
        self.__theta = theta
        self.__radius = radius

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_v(self):
        return self.__v

    def get_theta(self):
        return self.__theta

    def get_radius(self):
        return self.__radius

    def set_x(self, x):
        self.__x = x

    def set_y(self, y):
        self.__y = y

    def set_v(self, v):
        self.__v = v

    def set_theta(self, theta):
        self.__theta = theta


class Frame:
    def __init__(self, ball, mapping, canvas):
        self.__ball = ball
        self.__mapping = mapping
        self.__canvas = canvas
        self.__rebounds = 0
        self.__last_pos = None
        self.__circle = self.init_draw("blue")

    def init_draw(self, color):
        x = self.__ball.get_x()
        y = self.__ball.get_y()
        r = self.__ball.get_radius()
        i = self.__mapping.get_i(x)
        j = self.__mapping.get_j(y)
        return self.__canvas.create_oval(i-r, j-r, i+r, j+r, fill=color)

    def update_position(self):
        v = self.__ball.get_v()
        x = self.__ball.get_x()
        y = self.__ball.get_y()
        theta = self.__ball.get_theta()

        self.__last_pos = (x, y)

        if x > self.__mapping.get_xmax() or x < self.__mapping.get_xmin():
            # ball has reached left or right side of frame; bounce (change angle)
            theta = math.pi - theta
            self.__rebounds += 1

        if y > self.__mapping.get_ymax() or y < self.__mapping.get_ymin():
            # ball has reached top or bottom of frame
            theta = -theta
            self.__rebounds += 1

        self.__ball.set_theta(theta)

        # Updates (x,y) coords based on given formulae
        x += v * math.cos(theta)
        y += v * math.sin(theta)

        # Sets updated (x,y) coords
        self.__ball.set_x(x)
        self.__ball.set_y(y)

    def update_canvas(self):
        # move the ball
        x = self.__ball.get_x()
        y = self.__ball.get_y()
        r = self.__ball.get_radius()
        i = self.__mapping.get_i(x)
        j = self.__mapping.get_j(y)

        self.__canvas.coords(self.__circle, (i-r, j-r, i+r, j+r))

        # draw the trail
        i = self.__mapping.get_i(self.__last_pos[0])
        j = self.__mapping.get_j(self.__last_pos[1])
        self.__canvas.create_oval(i, j, i, j, fill='black')

    def get_rebounds(self):
        return self.__rebounds


def main():
    coord_in = input("Enter xmin,xmax,ymin,ymax (return for default -300,300,-300,300): ")
    info_in = input("Enter x0,y0,v,theta (return for default 0,0,70,30): ")

    # Takes user input as type str, separates desired values, and assigns to variables
    if coord_in == "":
        xmin, xmax, ymin, ymax = -300, 300, -300, 300
    else:
        xmin, xmax, ymin, ymax = map(float, coord_in.split())

    if info_in == "":
        x, y, v, theta = 0, 0, 70, (30 * math.pi / 180)
    else:
        info = info_in.split()
        info = [float(x) for x in info]
        x, y, v, theta = info[0], info[1], info[2], (info[3] * math.pi / 180)

    t_total = 0
    radius = 4
    width = 800
    ball = Ball(x, y, v * .1, theta, radius)
    m = Mapping_for_Tkinter(xmin, xmax, ymin, ymax, width)

    window = Tk()
    canvas = Canvas(window, width=m.get_width(), height=m.get_height(), bg="white")
    canvas.pack()

    frame = Frame(ball, m, canvas)

    while t_total < 150:
        time.sleep(.01)
        frame.update_position()
        frame.update_canvas()
        window.update()
        t_total += .1

    frame.init_draw("red")  # Draw red ball at simulation end
    print("Total number of rebounds is: %s" % frame.get_rebounds())
    window.mainloop()


if __name__ == "__main__":
    main()
