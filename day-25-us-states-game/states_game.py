import turtle
import pandas as pd

FONT = ("Fantasy", 7, "normal")
FONT_OVER = ("Fantasy", 70, "normal")
ALIGNMENT = "center"
states_path = "50_states.csv"
states_cor = pd.read_csv(states_path)
states_names = set(states_cor.state)


def state_coordinates(state_name):
    result = states_cor[states_cor.state == state_name]
    x_cor = result.x.item()
    y_cor = result.y.item()
    return x_cor, y_cor


image = "blank_states_img.gif"

screen = turtle.Screen()
screen.tracer(0)
screen.title("U.S. States Game")
screen.setup(width=800, height=550)

screen.addshape(image)
turtle.shape(image)
screen.update()
score = 0

while states_names:
    screen.update()
    answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="Input state's name")
    screen.update()

    # closing app
    if answer_state is None:
        break

    if answer_state.title() in states_names:
        answer_state = answer_state.title()
        x, y = state_coordinates(answer_state)
        states_names.remove(answer_state)

        # adding state into map
        new_state_sign = turtle.Turtle()
        new_state_sign.hideturtle()
        new_state_sign.penup()
        new_state_sign.goto(x, y)
        new_state_sign.color("black")
        new_state_sign.write(f"{answer_state}", move=False, align=ALIGNMENT, font=FONT)
        score += 1
    else:
        print(f"There isn't such a state like {answer_state}")
        continue


# GOOD JOB SIGN
end_sign = turtle.Turtle()
end_sign.hideturtle()
end_sign.penup()
end_sign.goto(0, 0)
end_sign.color("black")
end_sign.write(f"WELL DONE", move=False, align=ALIGNMENT, font=FONT_OVER)
screen.update()

to_learn = pd.DataFrame(states_names)
to_learn.to_csv("states_to_learn.csv")
print("Check your folder to familiarize yourself with states you didn't know :)")

screen.exitonclick()
# to
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop() # dzięki temu okno się nie zamyka zaraz po wyświetleniu zawartości
