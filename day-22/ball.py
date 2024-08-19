from turtle import Turtle
import random
MOVE_DISTANCE = 10


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.goto(0, 0)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1
        # self.random_direction()
        # self.move_ball()

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_ball(self):
        self.goto(0, 0)
        self.bounce_y()
        self.bounce_x()
        self.move_speed = 0.1

    # def random_direction(self):
    #     ran_dir = random.randrange(45, 315, 15)
    #     self.setheading(ran_dir)
    #
    # def wall_hit(self):
    #     new_dir = 360 - self.heading()
    #     self.setheading(new_dir)
    #
    # def move_ball(self):
    #     self.forward(MOVE_DISTANCE)


        # X_POS = random.randrange(-180, 180, 20)
        # Y_POS = random.randrange(-180, 180, 20)
        # self.goto(x=X_POS, y=Y_POS)
