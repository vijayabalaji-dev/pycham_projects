from turtle import Turtle


class Scoreboard(Turtle):
    score = 0

    def __init__(self, pos):
        super().__init__()
        self.color("#fff")
        self.penup()
        self.hideturtle()
        self.goto(pos)
        self.print()

    def print(self):
        self.write(f"Score: {self.score}", False, font=("verdana", 15, "normal"))

    def add_score(self):
        self.clear()
        self.score += 1
        self.print()
