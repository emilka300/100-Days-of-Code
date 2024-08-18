from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
FONT = "Arial"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letter_list  = [choice(letters) for _ in range(randint(8, 10))]
    symbols_list = [choice(symbols) for _ in range(randint(2, 4))]
    numbers_list = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = letter_list + symbols_list + numbers_list
    shuffle(password_list)

    generated_password = "".join(password_list)

    password_entry.insert(0, generated_password)
    pyperclip.copy(generated_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = wb_entry.get()
    email = u_name_entry.get()
    password = password_entry.get()

    if website and password:
        to_save = f"{website} | {email} | {password}\n"

        answer = messagebox.askyesno(title=website, message=f"Are details correct? \nEmail: {email}\nPassword: {password}")
        if answer:
            f = open(f"passwords.txt", "a")
            f.write(to_save)
            f.close()
            password_entry.delete(0, 'end')
            wb_entry.delete(0, 'end')
            wb_entry.focus()
    else:
        messagebox.showinfo(title="Oh no!", message="You've left some fields empty! \n"
                                                    "Please input all data before saving.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
padlock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=padlock_img)
canvas.grid(column=1, row=0)

# labels
website = Label(text="Website:", font=(FONT, 10), bg="white")
website.grid(column=0, row=1)

u_name = Label(text="Email/Username:", font=(FONT, 10), bg="white")
u_name.grid(column=0, row=2)

password = Label(text="Password:", font=(FONT, 10), bg="white")
password.grid(column=0, row=3)

# entries
wb_entry = Entry(width=45)
wb_entry.grid(column=1, row=1, columnspan=2)

u_name_entry = Entry(width=45)
u_name_entry.grid(column=1, row=2, columnspan=2)
u_name_entry.insert(0, "emilka300@gmail.com")

password_entry = Entry(width=27)
password_entry.grid(column=1, row=3)

# buttons
g_password_button = Button(text="Generate Password", command=generate_password)
g_password_button.grid(sticky="W", column=2, row=3)

add_button = Button(text="Add", width=45, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()
