from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 15, "normal")
THE_END_FONT = ('Courier', 30, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = -1
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.speed("fastest")
        self.increase_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.color("red")
        self.goto(0, 0)
        self.write(f"GAME OVER", move=False, align=ALIGNMENT, font=THE_END_FONT)


