import graphics
import math
from graphics import *

# def branch(start, lineLength):
#     print('x2:', x2 - starting_length * (3 / 4))
#     print('y2:', y2 - starting_length * (3 / 4))
#     end_point = Point(x2 - (starting_length * (3 / 4)), y2 - (starting_length * (3 / 4)))
#     branch1 = Line(start_point, end_point)
#     branch1.setFill("green")
#     branch1.setWidth(2)
#     branch1.draw(win)
#
#     x2 = x2 + (starting_length * (3 / 4))
#     y2 = y2 - (starting_length * (3 / 4))
#     print('x2:', x2)
#     print('y2:', y2)
#     end_point = Point(x2, y2)
#     branch2 = Line(start_point, end_point)
#     branch2.setFill("yellow")
#     branch2.setWidth(2)
#     branch2.draw(win)

def change(hypot_length):
    c = hypot_length ** 2 / 2
    a = math.sqrt(c)
    return a

def main(x,y):
    x_window_size = x
    y_window_size = y
    starting_length = 40

    win = GraphWin("Tree",x_window_size,y_window_size)
    win.setBackground("gray")


    start_point = Point(x_window_size/2,y_window_size)


    x2 = 100
    y2 = y_window_size - starting_length
    end_point = Point(x2,y2)

    trunk = Line(start_point, end_point)
    trunk.setWidth(3)
    trunk.draw(win)

    start_point = end_point

    print("New x: ", start_point.getX() + change(30))

#    branch(start_point, starting_length )


    win.getMouse()
    win.close()


main(400,400)