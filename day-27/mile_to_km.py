from tkinter import *


def button_click():
    inputted_text = int(entry.get())
    km_value = int(inputted_text * 1.609344)
    number.config(text=km_value)


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=150)
window.config(padx=20, pady=40)

entry = Entry(width=7)
entry.grid(column=1, row=0)

miles = Label(text="Miles", font=("Arial", 10))
miles.grid(column=2, row=0)

equal = Label(text="is equal to", font=("Arial", 10))
equal.grid(column=0, row=1)

number = Label(text="0", font=("Arial", 10))
number.config(padx=30, pady=10)
number.grid(column=1, row=1)

km = Label(text="Km", font=("Arial", 10))
km.grid(column=2, row=1)

button = Button(text="Calculate", command=button_click)
button.grid(column=1, row=2)

window.mainloop()
