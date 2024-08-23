from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.canvas = Canvas(width=300, height=250)
        self.question = self.canvas.create_text(150, 125, text="question", width=280, font=("Arial", 20, "italic")
                                                , fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=30)

        # label
        self.score = Label(text=f"Score: {self.quiz.score}", font=("Arial", 10, "bold"), bg=THEME_COLOR, fg="white")
        self.score.grid(column=1, row=0)
        self.score.config(padx=20, pady=20)

        # buttons
        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true)
        self.true_button.grid(column=0, row=2, padx=20)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false)
        self.false_button.grid(column=1, row=2, padx=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.configure(bg="white")
        if self.quiz.still_has_questions():
            q_test = self.quiz.next_question()
            self.score.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.question, text=q_test)
        else:
            self.canvas.itemconfig(self.question, text="You've reached to the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true(self):
        if self.quiz.check_answer("true") is True:
            self.canvas.configure(bg="green")
        else:
            self.canvas.configure(bg="red")
        self.window.after(1000, self.get_next_question)

    def false(self):
        if self.quiz.check_answer("false") is True:
            self.canvas.configure(bg="green")
        else:
            self.canvas.configure(bg="red")
        self.window.after(1000, self.get_next_question)


