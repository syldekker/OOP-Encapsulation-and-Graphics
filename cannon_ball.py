from Mapping_for_Tkinter import Mapping_for_Tkinter
from tkinter import *
import math
import time


class Ball:
    def __init__(self, x0, y0, v, theta, radius, strength):
        self.__x = x0
        self.__y = y0
        self.__v = v
        self.__theta = theta
        self.__radius = radius
        self.__strength = strength

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

    def get_strength(self):
        return self.__strength

    def set_x(self, x):
        self.__x = x

    def set_y(self, y):
        self.__y = y

    def set_v(self, v):
        self.__v = v

    def set_theta(self, theta):
        self.__theta = theta


class Frame:
    def __init__(self, ball, mapping, canvas, interval, g=9.8):
        self.__ball = ball
        self.__mapping = mapping
        self.__canvas = canvas
        self.__rebounds = 0
        self.__last_pos = None
        self.__circle = self.init_draw("blue")
        self.__ended = False
        self.__t = 0
        self.__x0 = ball.get_x()
        self.__y0 = ball.get_y()
        self.__interval = interval
        self.__g = g

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

        if x > self.__mapping.get_xmax() or x < self.__mapping.get_xmin() or v < .01:
            # ball has reached left or right side of frame or
            # velocity gets too low; end simulation
            self.__ended = True

        if y < self.__mapping.get_ymin():
            # ball has reached bottom of frame; start new parabola starting with x0,y0
            self.__rebounds += 1
            self.__x0 = x
            self.__y0 = y
            self.__t = 0
            v = v * self.__ball.get_strength()
            self.__ball.set_v(v)  # update v outside local

        self.__t += self.__interval

        x = self.__x0 + v * math.cos(theta) * self.__t
        y = self.__y0 + v * math.sin(theta) * self.__t - (self.__g/2) * self.__t ** 2

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

    def ended(self):
        return self.__ended


def main():
    in_str = input("Enter v,theta(0,90),strength (return for default 70,60,0.75): ")

    if in_str == "":
        v, theta, strength = 70, 60, 0.75
    else:
        v, theta, strength = map(float, in_str.split())

    x, y = 0, 0
    radius = 4
    t_total = 0
    ball = Ball(x, y, v, theta * math.pi / 180, radius, strength)
    m = Mapping_for_Tkinter(0.0, 1200.0, 0.0, 400.0, 1200)

    window = Tk()
    canvas = Canvas(window, width=m.get_width(), height=m.get_height(), bg="white")
    canvas.pack()

    frame = Frame(ball, m, canvas, 0.1)

    while not frame.ended():
        time.sleep(.02)
        frame.update_position()
        frame.update_canvas()
        window.update()
        t_total += .11  # time counter

    frame.init_draw("red")  # turn ball red at simulation end
    print("Total number of rebounds is: %s" % frame.get_rebounds())
    print("Total time is: %ss" % t_total)
    window.mainloop()


if __name__ == "__main__":
    main()
