import json
from os.path import isfile
from tkinter import *


def show_passwords():
    new_win = Tk()
    new_win.title("All Password")
    new_win.minsize(100, 100)
    new_win.config(padx=50, pady=50)

    new_title = Label(new_win, text="All Passwords", fg="green", font=20)
    new_title.grid(row=0, column=1)

    label = Label(new_win)
    label.grid(row=1, column=1)

    if isfile("data.json"):
        with open("data.json") as file:
            data = json.load(file)
            formatted = ""
            for item in data.items():
                formatted += f"{item[0]} | {item[1]['username']} | {item[1]['password']}\n"
                print(formatted)
            label.config(text=formatted, font=20)
    new_win.mainloop()
