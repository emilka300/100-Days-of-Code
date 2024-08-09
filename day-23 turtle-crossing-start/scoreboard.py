from turtle import Turtle
FONT = ("Courier", 24, "normal")
ALIGNMENT = "left"
ALIGNMENT_OVER = "center"


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.color("black")
        self.hideturtle()
        self.penup()
        self.update_level()
        self.move_speed = 0.1

    def game_over(self):
        self.color("red")
        self.goto(0, 0)
        self.move_speed = 0.1
        self.write(f"GAME OVER", move=False, align=ALIGNMENT_OVER, font=FONT)

    def update_level(self):
        self.clear()
        self.goto(-200, 220)
        self.write(f"Level: {self.level}", move=False, align=ALIGNMENT, font=FONT)

    def next_level(self):
        self.level += 1
        self.update_level()
        self.move_speed *= 0.8

