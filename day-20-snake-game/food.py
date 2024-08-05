from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("blue")
        self.speed("fastest")
        self.move_food()

    def move_food(self):
        X_POS = random.randrange(-180, 180, 20)
        Y_POS = random.randrange(-180, 180, 20)
        self.goto(x=X_POS, y=Y_POS)
