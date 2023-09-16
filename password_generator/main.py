import json
from os.path import isfile
from random import randint, choice, shuffle
from tkinter import *
from tkinter import messagebox

import pyperclip

from show_passwords import show_passwords
from search_password import search_password

# Password Generator Project

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    password_list += [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)

    gen_password = "".join(password_list)
    password.delete(0, END)
    password.insert(0, gen_password)
    pyperclip.copy(gen_password)


# *******************     add data to file    *********************

def write_to_file(data):
    with open("data.json", "w") as data_file:
        json.dump(data, data_file, indent=4)

def send_to_search():
    web_site = website.get()
    if web_site == "":
        messagebox.showerror(title="Error", message="please enter a value")
    else:
        search_password(web_site)
def add_data():
    web_site = website.get()
    user_name = username.get()
    pass_word = password.get()

    if pass_word == "" or user_name == "" or pass_word == "":
        messagebox.showerror(title="Oops!", message="Please don't leave columns empty")
    else:
        new_json = {
            web_site: {
                "username": user_name,
                "password": pass_word
            }
        }
        is_ok = messagebox.askokcancel(title=web_site, message=f"The details you entered"
                                                               f" \nEmail: {user_name} \nPassword: {pass_word} "
                                                               f"\nIs it okay to save?")
        if is_ok:
            # with open("data.txt", "a") as file:
            #     file.write(f"{web_site} | {user_name} | {pass_word} \n")

            if isfile("data.json"):
                with open("data.json") as data_file:
                    data = json.load(data_file)
                    data.update(new_json)
                    write_to_file(data)

            else:
                write_to_file(new_json)

            website.delete(0, END)
            password.delete(0, END)
            messagebox.showinfo(title=web_site, message="added successfully")


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, width=200, height=400)
img = PhotoImage(file="logo.png")

canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=1)

website_title = Label(text="Website: ")
website_title.grid(row=1, column=0)

website = Entry(width=27)
website.grid(row=1, column=1)
website.focus()

search = Button(text="Search", width=14, command=send_to_search)
search.grid(row=1, column=2)

username_title = Label(text="Email/ Username: ")
username_title.grid(row=2, column=0)

username = Entry(width=46)
username.grid(row=2, column=1, columnspan=2)
username.insert(0, "jvijayabalaji03082002@gmail.com")

password_title = Label(text="Password: ")
password_title.grid(row=3, column=0)

password = Entry(width=27)
password.grid(row=3, column=1)

generate_pswd_button = Button(text="Generate Password", command=generate_password)
generate_pswd_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=add_data)
add_button.grid(row=4, column=1, columnspan=2)

review = Button(text="show", width=20, command=show_passwords)
review.grid(row=5, column=1)

window.mainloop()
