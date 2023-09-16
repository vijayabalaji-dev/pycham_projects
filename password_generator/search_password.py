import json
from tkinter import messagebox


def search_password(name):
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title=name, message="No data found")
    except json.JSONDecodeError:
        messagebox.showerror(title=name, message="No data found")
    else:
        try:
            us_and_ps = data[name]
            print(us_and_ps)
        except KeyError:
            messagebox.showerror(title=name, message="No data found")
        else:
            messagebox.showinfo(title=name,
                                message=f"Username: {us_and_ps['username']}\nPassword: {us_and_ps['password']}")
