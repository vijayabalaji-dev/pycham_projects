from tkinter import *
import pandas as pd
import random as rd
import os.path as op

BACKGROUND_COLOUR = "#B1DDC6"
data = {}

# reading csv
dataframe = ""
if op.isfile("./data/words_to_learn.csv"):
    dataframe = pd.read_csv("./data/words_to_learn.csv")
else:
    dataframe = pd.read_csv("./data/french_words.csv")
word_dict = dataframe.to_dict(orient="records")


def on_click():
    global data, timer
    data = rd.choice(word_dict)
    window.after_cancel(timer)
    canvas.itemconfig(canvas_image, image=French_img)
    canvas.itemconfig(language, text="French", fill="black")
    canvas.itemconfig(word, text=data["French"], fill="black")
    timer = window.after(3000, to_english)


def to_english():
    canvas.itemconfig(canvas_image, image=English_img)
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(word, text=data["English"], fill="white")


def on_click_green():
    word_dict.remove(data)
    new_df = pd.DataFrame(word_dict)
    new_df.to_csv("./data/words_to_learn.csv", index=False)
    on_click()


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOUR)

French_img = PhotoImage(file="images/card_front.png")
English_img = PhotoImage(file="images/card_back.png")
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOUR)
canvas_image = canvas.create_image(400, 264, image=French_img)
canvas.grid(row=0, column=0, columnspan=2)

timer = window.after(3000, to_english)

no_button_image = PhotoImage(file="./images/wrong.png")
no_button = Button(image=no_button_image, highlightthickness=0, command=on_click)
no_button.grid(row=1, column=0)

yes_button_image = PhotoImage(file="./images/right.png")
yes_button = Button(image=yes_button_image, highlightthickness=0, command=on_click_green)
yes_button.grid(row=1, column=1)

language = canvas.create_text(400, 150, font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, font=("Ariel", 60, "bold"))

on_click()

window.mainloop()
