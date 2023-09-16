from tkinter import *

from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizBoard:

    def __init__(self, quiz_q: QuizBrain):
        self.quiz = quiz_q
        self.timer = None
        self.window = Tk()
        self.window.title("Quiz")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score_label = Label(text=f"Score: {self.quiz.score}", bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250)
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

        self.text_canvas = self.canvas.create_text(150, 125, width=280,
                                                   font=("Arial", 20, "italic"))

        true_img = PhotoImage(file="images/true.png")
        false_img = PhotoImage(file="images/false.png")

        self.true_button = Button(image=true_img, highlightthickness=0, bg=THEME_COLOR,
                                  command=self.true_button_clicked)
        self.false_button = Button(image=false_img, highlightthickness=0, bg=THEME_COLOR,
                                   command=self.false_button_clicked)
        self.true_button.grid(row=2, column=0)
        self.false_button.grid(row=2, column=1)
        self.next_question()

        self.window.mainloop()

    def true_button_clicked(self):
        is_right = self.quiz.check_answer("True")
        if is_right:
            self.canvas.configure(bg="green")
        else:
            self.canvas.configure(bg="red")
        self.score_label.config(text=f"Score: {self.quiz.score}")
        self.call_next_question()

    def false_button_clicked(self):
        is_right = self.quiz.check_answer("False")
        if is_right:
            self.canvas.configure(bg="green")
        else:
            self.canvas.configure(bg="red")
        self.score_label.config(text=f"Score: {self.quiz.score}")
        self.call_next_question()

    def call_next_question(self):
        self.window.after(1000, self.next_question)
        if not self.quiz.still_has_questions():
            self.false_button.config(state="disabled")
            self.true_button.config(state="disabled")

    def next_question(self):
        self.canvas.configure(bg="white")
        self.canvas.itemconfig(self.text_canvas, text=self.quiz.next_question())
