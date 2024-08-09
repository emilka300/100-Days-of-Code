from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.random_y = random.randrange(-230, 230)
        self.goto(280, self.random_y)
        self.color(random.choice(COLORS))
        self.turtlesize(stretch_len=2, stretch_wid=1)

    def move(self):
        new_x = self.xcor() - STARTING_MOVE_DISTANCE
        self.goto(new_x, self.random_y)

    def reset_car(self):
        self.hideturtle()







