from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
CHECKMARK = "✔"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
CHECKS = ""
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    window.after_cancel(timer)
    check_mark.config(text="")
    title_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text=f"00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start():
    global REPS
    work_sek = WORK_MIN * 60
    short_break_sek = SHORT_BREAK_MIN * 60
    long_break_sek = LONG_BREAK_MIN * 60

    REPS += 1
    if REPS % 8 == 0:
        title_label.config(text="Long break", fg=RED)
        REPS = 0
        count_down(long_break_sek)

    elif REPS % 2 == 0:
        title_label.config(text="Short break", fg=PINK)
        count_down(short_break_sek)
    else:
        title_label.config(text="Work time", fg=GREEN)
        count_down(work_sek)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global CHECKS
    count_min = math.floor(count/60)
    count_sek = count % 60
    # resolves issue with lack of 0 before "9" ec. => "09" "00"
    if count_sek < 10:
        count_sek = f"0{count_sek}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sek}")
    if count > 0:
        global timer
        # window.after(1000 -> tike to wait between calling func, count_down -> function to call, count - 1 -> param)
        timer = window.after(1000, count_down, count - 1)
    else:
        start()
        if REPS % 2 == 0:
            CHECKS += CHECKMARK
            check_mark.config(text=CHECKS)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1, padx=100)


# labels
title_label = Label(text="Timer", font=(FONT_NAME, 40, "bold"), bg=YELLOW, fg=GREEN)
title_label.grid(column=1, row=0)

# buttons
button_start = Button(text="Start", command=start)
button_start.grid(column=0, row=2)

button_reset = Button(text="Reset", command=reset)
button_reset.grid(column=2, row=2)

# checkmark
check_mark = Label(font=(FONT_NAME, 10, "bold"), bg=YELLOW, fg=GREEN)
check_mark.grid(column=1, row=3)

window.mainloop()
