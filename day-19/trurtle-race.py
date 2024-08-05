import turtle
import turtle as t
import random

screen = t.Screen()
screen.setup(width=500, height=400)
is_race_on = False
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: "
                                                          "(red/orange/yellow/green/blue/purple)")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
colors_iter = iter(colors)
y_positions = [-100, -60, -20, 20, 60, 100]
turtles = []

for turtle_index in range(0, 6):
    new_turtle = t.Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(next(colors_iter))
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        random_dist = random.randint(0, 10)
        turtle.forward(random_dist)

screen.exitonclick()

