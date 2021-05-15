from Mapping_for_Tkinter import Mapping_for_Tkinter
from tkinter import *
from math import *


def main():
    # formula input
    formula = input("Enter math formula (using x variable): ")
    coords = input("Enter xmin, xmax, ymin, ymax (return for default -5,5,-5,5): ")
    if coords == "":
        xmin, xmax, ymin, ymax = (-5., 5., -5., 5.)
    else:
        xmin, xmax, ymin, ymax = map(float, coords.split(" "))
    while xmax <= xmin:
        xcoords = input("Your max is invalid (xmax<=xmin). Re-enter correct xmin,xmax: ")
        xmin, xmax = map(float, xcoords.split(" "))
    while ymax <= ymin:
        ycoords = input("Your ymax is invalid (ymax<=ymin). Re-enter correct ymin,ymax: ")
        ymin, ymax = map(float, ycoords.split(" "))

    m = Mapping_for_Tkinter(xmin, xmax, ymin, ymax, 800)

    window = Tk()
    canvas = Canvas(window, width=m.get_width(), height=m.get_height(), bg="white")
    canvas.pack()

    for i in range(m.get_width()):
        # eval and draw formula
        x = m.get_x(i)
        y = eval(formula)
        canvas.create_rectangle((m.get_i(x), m.get_j(y)) * 2, outline="blue")

    if xmin <= 0 <= xmax:
        # draw x axis
        y = (m.get_ymax() + m.get_ymin()) // 2
        j = m.get_j(y)
        canvas.create_line(0, j, m.get_width(), j)

    if ymin <= 0 <= ymax:
        # draw y axis
        x = (m.get_xmax() + m.get_xmin()) // 2
        i = m.get_i(x)
        canvas.create_line(i, 0, i, m.get_height())

    window.mainloop()

if __name__ == "__main__":
    main()