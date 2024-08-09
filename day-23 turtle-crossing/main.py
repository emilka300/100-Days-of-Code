import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import ScoreBoard

screen = Screen()
screen.bgcolor("white")
screen.title("Turtle Crossing")
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Player()

score_board = ScoreBoard()

cars = []

screen.listen()
screen.onkey(fun=turtle.move_up, key="Up")

loop = 0
game_is_on = True
while game_is_on:
    loop += 1
    time.sleep(score_board.move_speed)
    if loop == 6:
        car = CarManager()
        cars.append(car)
        loop = 0
    for car in cars:
        car.move()
        if car.xcor() == -300:
            cars.remove(car)
            car.reset_car()
            del car
            continue
        if turtle.distance(car) < 15:
            score_board.game_over()
            game_is_on = False
    if turtle.ycor() == 240:
        score_board.next_level()
        turtle.goto_start_pos()

    screen.update()

screen.exitonclick()

