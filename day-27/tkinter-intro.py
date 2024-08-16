from tkinter import *
# POSITIONING (they make element visible)
# .pack()  - geometry-management mechanism; default = "top"; each other element will be under
# .place() - I give x&y coordinates
#   (0, 0) means high left corner
#   (100, 200) means 100 to right and 200 down)
# .grid()  - depends on number of elements;
#   each element starts from left high corner (0, 0),
#   but next element will appear in correspondence to other elements
# you CAN'T mix pack() and grid() -> error

# PADDING - space around element
# .config(padx=20, pady=20)


def button_click():
    inputted_text = text_input.get()
    my_label.config(text=inputted_text)


window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

# changing values after initialisation
my_label["text"] = "New Text"
my_label.config(text="New Text")

# button
button_1 = Button(text="Click Me", command=button_click)
button_1.grid(column=1, row=1)

button_2 = Button(text="Click Me", command=button_click)
button_2.grid(column=2, row=0)

# entry
text_input = Entry(width=10)
text_input.grid(column=3, row=2)


window.mainloop()




