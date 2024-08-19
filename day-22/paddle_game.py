# score-board + middle line
# ball + players
# main with rules and screen

# PADDLE GAME

# 7) detect when paddle misses
# 8) keep score

import turtle as t
from paddle import Paddle
from ball import Ball
from score_board import ScoreBoard
import time

screen = t.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
game_is_on = True

# create and move a paddle
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

# create the ball and make it move
ball = Ball()

# create a scoreboard
score_board = ScoreBoard()

# control the paddle
screen.listen()
screen.onkey(fun=r_paddle.move_up, key="Up")
screen.onkey(fun=r_paddle.move_down, key="Down")
screen.onkey(fun=l_paddle.move_up, key="w")
screen.onkey(fun=l_paddle.move_down, key="s")

# move the paddle
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # detect when paddle misses
    if ball.xcor() < -380:
        ball.reset_ball()
        score_board.increase_score_r()

    if ball.xcor() > 380:
        ball.reset_ball()
        score_board.increase_score_l()

    # detect collision with wall
    if ball.ycor() < -280 or ball.ycor() > 280:
        ball.bounce_y()

    # detect collision with r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # if l_paddle.distance(ball) <= 50:
    #     ball.wall_hit()
    # if r_paddle.distance(ball) <= 50:
    #     ball.wall_hit()

screen.exitonclick()
