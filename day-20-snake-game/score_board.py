from turtle import Turtle
import os

ALIGNMENT = "center"
FONT = ('Courier', 15, "normal")
THE_END_FONT = ('Courier', 30, "normal")
HIGHEST_SCORE_PATH = "highest_score.txt"


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.speed("fastest")
        if not os.path.exists(HIGHEST_SCORE_PATH):
            self.best_score = 0
            self.save_score()
        else:
            r = open(HIGHEST_SCORE_PATH, "r")
            self.best_score = int(r.read())
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}, Best score: {self.best_score}", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()

    def reset(self):
        if self.score > self.best_score:
            self.best_score = self.score
            self.save_score()
        self.score = 0
        self.update_score()

    def game_over(self):
        self.color("red")
        self.goto(0, 0)
        self.write(f"GAME OVER", move=False, align=ALIGNMENT, font=THE_END_FONT)

    def save_score(self):
        f = open(HIGHEST_SCORE_PATH, "w")
        f.write(f'{self.best_score}')
