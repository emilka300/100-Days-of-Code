from tkinter import *
import pandas as pd
import random
import os

FONT = "Ariel"
BACKGROUND_COLOR = "#B1DDC6"
timer = None
current_card = {}
words_dict = {}


# ------------------------------ DATA --------------------------------- #
try:
    words = pd.read_csv("data/words_to_learn.csv")
    words_dict = words.to_dict(orient="records")
except FileNotFoundError:
    words = pd.read_csv("data/french_words.csv")
    words_dict = words.to_dict(orient="records")


# ------------------------- BUTTONS ACTION ---------------------------- #
def next_card():
    global timer, current_card
    timer = window.after(3000, translation)
    try:
        current_card = random.choice(words_dict)
    except IndexError:
        print("You've reached to the end of list.")
        exit()
    else:
        canvas.itemconfig(card, image=front_card_img)
        canvas.itemconfig(word, text=current_card["French"], fill="black")
        canvas.itemconfig(language, text="French", fill="black")


def translation():
    global timer, current_card
    canvas.itemconfig(card, image=back_card_img)
    canvas.itemconfig(word, text=current_card["English"], fill="white")
    canvas.itemconfig(language, text="English", fill="white")


def right():
    global timer, current_card
    window.after_cancel(timer)
    try:
        words_dict.remove(current_card)
    except ValueError:
        print(f"words_dict {words_dict} ; current_card {current_card}")
    else:
        to_learn_pd = pd.DataFrame(words_dict)
        to_learn_pd.to_csv("data/words_to_learn.csv", index=False)
    finally:
        next_card()


def wrong():
    global timer
    window.after_cancel(timer)
    next_card()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_card_img = PhotoImage(file="images/card_front.png")
card = canvas.create_image(400, 263, image=front_card_img)

back_card_img = PhotoImage(file="images/card_back.png")

language = canvas.create_text(400, 150, text="", fill="black", font=(FONT, 40, "italic"))
word = canvas.create_text(400, 263, text="", fill="black", font=(FONT, 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# buttons
right_image = PhotoImage(file="images/right.png")
unknown_button = Button(image=right_image, highlightthickness=0, command=right)
unknown_button.grid(column=0, row=1)

wrong_image = PhotoImage(file="images/wrong.png")
known_button = Button(image=wrong_image, highlightthickness=0, command=wrong)
known_button.grid(column=1, row=1)

next_card()

window.mainloop()
