# w = forwards
# s = backwards
# a = counter-clockwise
# d = clockwise
# c = clean

import turtle as t
tim = t.Turtle()
screen = t.Screen()


def forwards():
    tim.forward(10)


def backwards():
    tim.backward(10)


def clockwise():
    tim.right(10)


def counter_clockwise():
    tim.left(10)


def clean():
    screen.resetscreen()


screen.listen()
screen.onkey(key="w", fun=forwards)
screen.onkey(key="s", fun=backwards)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="c", fun=clean)


screen.exitonclick()

