from turtle import Turtle
import os.path


class ScoreBoard(Turtle):
    score = 0

    def __init__(self):
        super().__init__()
        self.high_score = 0
        if os.path.isfile("data.txt"):
            with open("data.txt") as file:
                self.high_score = int(file.read())
        else:
            with open("data.txt", mode="w") as file:
                file.write(str(0))

        self.color("#fff")
        self.penup()
        self.hideturtle()
        self.goto(0, 275)
        self.score_print()

    def score_print(self):
        self.write(f"Score: {self.score} HighScore {self.high_score}", align="center", font=('Arial', 15, 'normal'))

    def add_score(self):
        self.score += 1
        self.clear()
        self.score_print()

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.clear()
        self.score_print()

