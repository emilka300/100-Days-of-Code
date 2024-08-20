from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

FONT = "Arial"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letter_list = [choice(letters) for _ in range(randint(8, 10))]
    symbols_list = [choice(symbols) for _ in range(randint(2, 4))]
    numbers_list = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = letter_list + symbols_list + numbers_list
    shuffle(password_list)

    generated_password = "".join(password_list)

    password_entry.insert(0, generated_password)
    pyperclip.copy(generated_password)


# --------------------------- SEARCH PASSWORD ------------------------------ #
def search():
    website = wb_entry.get().title()
    try:
        f = open(f"passwords.json", "r")
        passwords = json.load(f)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message=f"No Data File Found.")
    else:
        if website in passwords:
            searched_password = passwords[website]["password"]
            searched_email = passwords[website]["email"]
            messagebox.showinfo(title="Your data", message=f"Email: {searched_email}\nPassword: {searched_password}")
        else:
            messagebox.showinfo(title="No data found.", message=f"You haven't saved entries for {website}.")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = wb_entry.get().title()
    email = u_name_entry.get()
    password = password_entry.get()

    if website and password:
        to_save = {website: {"email": email,
                             "password": password}
                   }

        answer = messagebox.askyesno(title=website,
                                     message=f"Are details correct? \nEmail: {email}\nPassword: {password}")
        if answer:
            try:
                f = open(f"passwords.json", "r")
                data = json.load(f)
            except FileNotFoundError:
                f = open(f"passwords.json", "w")
                json.dump(to_save, f, indent=4)
                f.close()
            else:
                data.update(to_save)
                f.close()
                f = open(f"passwords.json", "w")
                # json.dump(data to save in json, location to save)
                json.dump(data, f, indent=4)
            finally:
                password_entry.delete(0, 'end')
                wb_entry.delete(0, 'end')
                wb_entry.focus()
                messagebox.showinfo(title="Done!", message="Password saved.")
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
wb_entry = Entry(width=27)
wb_entry.grid(column=1, row=1)

u_name_entry = Entry(width=45)
u_name_entry.grid(column=1, row=2, columnspan=2)
u_name_entry.insert(0, "emilka300@gmail.com")

password_entry = Entry(width=27)
password_entry.grid(column=1, row=3)

# buttons
g_password_button = Button(text="Generate Password", command=generate_password)
g_password_button.grid(sticky="W", column=2, row=3)

search_button = Button(text="Search", command=search, width=16)
search_button.grid(column=2, row=1)

add_button = Button(text="Add", width=45, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
