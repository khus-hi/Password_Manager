from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8,10)
    nr_symbols = random.randint(2,4)
    nr_numbers = random.randint(2,4)

    password_letter = [random.choice(letters)for _ in range( nr_letters)]
    password_symbols = [random.choice(symbols)for _ in range( nr_symbols)]
    password_numbers = [random.choice(numbers)for _ in range( nr_numbers)]

    password_list=password_letter+password_symbols+password_numbers

    random.shuffle(password_list)


    password = "".join(password_list)
    entry_password.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = entry_web.get()
    email = entry_email.get()
    password = entry_password.get()

    if len(website)==0 or len(email)==0:
        messagebox.showinfo(title="Oops",message="Please make sure you haven't left any field empty")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\nemail: {email}\n"
                                                              f"password: {password}\n Is it ok to save?")

        if is_ok == True:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                entry_web.delete(0, END)
                entry_password.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

label_web = Label(text="Website:")
label_web.grid(column=0, row=1)

label_email = Label(text="Email/Username:")
label_email.grid(column=0, row=2)

label_password = Label(text="Password:")
label_password.grid(column=0, row=3)

entry_web = Entry(width=51)
entry_web.grid(column=1, row=1, columnspan=2)
entry_web.focus()

entry_email = Entry(width=51)
entry_email.grid(column=1, row=2, columnspan=2)
entry_email.insert(0, "xyz@gmail.com")
entry_password = Entry(width=33)
entry_password.grid(column=1, row=3)

button_password = Button(text="Generate Password", width=14,command=generate_password)
button_password.grid(column=2, row=3)

button_add = Button(text="Add", width=44, command=save)
button_add.grid(column=1, columnspan=2, row=4)

window.mainloop()
