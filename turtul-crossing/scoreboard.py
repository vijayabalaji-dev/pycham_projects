from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    level = 0

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("#000")
        self.goto(-280,260)
        self.score_write()

    def score_write(self):
        self.write(f"Level: {self.level}", False, font=FONT)

    def add_level(self):
        self.level += 1
        self.clear()
        self.score_write()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", False, font=FONT)


