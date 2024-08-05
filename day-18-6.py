import turtle as t
import random

screen = t.Screen()
tim = t.Turtle()
tim.speed("fastest")
t.colormode(255)

########### Challenge 6 - Spirograph ########
colours = ["CornflowerBlue", "DarkOrchid"]


def draw_spirograph(size_of_gap, size):
    for r in range(int(360/size_of_gap)):
        tim.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        tim.circle(size)
        tim.right(size_of_gap)


draw_spirograph(10, 50)
draw_spirograph(15, 100)

screen.exitonclick()
