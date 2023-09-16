from tkinter import *

window = Tk()
window.minsize(width=500, height=400)
window.title("My first GUI")
window.config(padx=100, pady=100)

my_label = Label(text="I am a label", font=("arial", 20, "bold"))
my_label.grid(column=0, row=0)


def change_text():
    my_label["text"] = user_input.get()


button = Button(text="Click Me", command=change_text)
button.grid(column=1, row=1)
button.config(padx=50)

button1 = Button(text="Click Me", command=change_text)
button1.grid(column=2, row=0)

user_input = Entry(width=30)
user_input.grid(column=3, row=3)


window.mainloop()
