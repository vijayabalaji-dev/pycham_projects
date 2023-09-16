from tkinter import *
from math import floor

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 20
reps = 1
tick_mark = ""
timer_running = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer_running)
    timer.config(text="Timer")
    global reps
    reps = 1
    global tick_mark
    tick_mark = ""
    canvas.itemconfig(time, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    print(reps)
    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    if reps % 2 != 0:
        timer.config(text="Work", fg=GREEN)
        count_down(work_sec)
        tick.config(text="")
    if reps == 8:
        timer.config(text="Long Break", fg=RED)
        count_down(long_break)
    elif reps % 2 == 0:
        global tick_mark
        tick_mark += "✔"
        timer.config(text="Break", fg=PINK)
        tick.config(text=tick_mark)
        count_down(short_break)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    # num / 60 gives min
    # num % 60 gives remaining sec
    count_min = floor(count / 60)
    if count_min < 10:
        count_min = f"0{count_min}"
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(time, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer_running
        timer_running = window.after(1000, count_down, count - 1)
    else:
        global reps
        reps = reps + 1
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("pomodora")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=img)
time = canvas.create_text(103, 140, text="00.00", font=(FONT_NAME, 20, "bold"), fill="white")
canvas.grid(row=1, column=1)

timer = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 30, "bold"), bg=YELLOW)
timer.grid(row=0, column=1)

start = Button(text="Start", highlightthickness=0, command=start_timer)
start.grid(row=3, column=0)

reset = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset.grid(row=3, column=2)

tick = Label(fg=GREEN, bg=YELLOW, font=20)
tick.grid(row=4, column=1)

window.mainloop()
