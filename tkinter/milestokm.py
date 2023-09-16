from tkinter import *


def calculate():
    u_mile = float(user_input.get())
    km = str(round(u_mile*1.609))
    answer.config(text=km)


window = Tk()
window.minsize(width=400, height=200)
window.config(padx=50, pady=50)

user_input = Entry()
user_input.grid(row=0, column=1)

is_equal_to = Label(text="is equal to", font=("arail", 15))
is_equal_to.grid(row=1, column=0)
is_equal_to.config(padx=20)

miles = Label(text="miles", font=("arail", 15))
miles.grid(row=0, column=2)
miles.config(padx=20)

answer = Label(text="0", font=("arail", 15))
answer.grid(row=1, column=1)
answer.config(padx=20)

km = Label(text="km", font=("arail", 15))
km.grid(row=1, column=2)
km.config(padx=20)

button = Button(text="calculate", command=calculate)
button.grid(row=2, column=1)


window.mainloop()
