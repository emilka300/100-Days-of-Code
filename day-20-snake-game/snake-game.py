# SNAKE GAME

import turtle as t
from snake import Snake
from food import Food
from score_board import ScoreBoard
import time

screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
game_is_on = True

# create snake
snake = Snake()

# detect collision with food
food = Food()

# create a scoreboard
score_board = ScoreBoard()

# control the snake
screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

# move the snake
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collision with food
    if snake.head.distance(food) <= 5:
        food.move_food()
        score_board.increase_score()
        snake.extend()

    # detect collision with wall
    if snake.head.xcor() < -280 or snake.head.xcor() > 280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
        game_is_on = False
        score_board.game_over()

    # detect collision with tail
    for segment in snake.snake[1:]:
        if snake.head.distance(segment) <= 5:
            game_is_on = False
            score_board.game_over()

screen.exitonclick()
