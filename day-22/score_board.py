from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 15, "normal")
FONT_SCORE = ('Courier', 30, "normal")
THE_END_FONT = ('Courier', 30, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_r = 0
        self.score_l = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.create_line()
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(0, 220)
        self.write(f"{self.score_l} : {self.score_r}", move=False, align=ALIGNMENT, font=FONT)
        self.goto(0, 260)
        self.write("SCORE", move=False, align=ALIGNMENT, font=FONT_SCORE)

    def create_line(self):
        for line_y in range(-260, 260, 40):
            self.goto(0, line_y)
            self.write(f"|", move=False, align=ALIGNMENT, font=FONT)

    def increase_score_r(self):
        self.score_r += 1
        self.update_score()

    def increase_score_l(self):
        self.score_l += 1
        self.update_score()

    def game_over(self):
        self.color("red")
        self.goto(0, 0)
        self.write(f"GAME OVER", move=False, align=ALIGNMENT, font=THE_END_FONT)

