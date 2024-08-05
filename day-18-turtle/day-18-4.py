import turtle as t
import random

tim = t.Turtle()

########### Challenge 4 - Random Walk ########

# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen",
#            "wheat", "SlateGray", "SeaGreen"]
direction = [0, 90, 180, 270]
t.colormode(255)
tim.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

tim.shape("circle")
tim.speed('fastest')
tim.pensize(10)
x = 2

while x > 1:
    # tim.color(random.choice(colours))
    tim.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    tim.setheading(random.choice(direction))
    tim.forward(30)

