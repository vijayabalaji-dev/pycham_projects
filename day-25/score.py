import turtle


class Score(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def state_write(self, x, y, text):
        self.goto(x, y)
        self.write(text)
