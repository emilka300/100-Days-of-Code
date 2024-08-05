import turtle as t
# 1) create a snake body
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        segment = t.Turtle(shape="square")
        segment.penup()
        segment.color("white")
        segment.goto(position)
        self.snake.append(segment)

    def extend(self):
        self.add_segment(self.snake[-1].position())

    def up(self):
        if self.head.heading() != 270:
            return self.head.setheading(90)

    def left(self):
        if self.head.heading() != 0:
            return self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            return self.head.setheading(0)

    def down(self):
        if self.head.heading() != 90:
            return self.head.setheading(270)

    def move(self):
        for seg_num in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[seg_num - 1].xcor()
            new_y = self.snake[seg_num - 1].ycor()
            self.snake[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)




