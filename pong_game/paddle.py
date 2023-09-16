from turtle import Turtle


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("#fff")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.speed("fastest")

    def paddle_up(self):
        if self.ycor() < 240:
            new_y = self.ycor() + 20
            self.set_paddle_pos(self.xcor(), new_y)

    def set_paddle_pos(self, x, y):
        self.goto(x, y)

    def paddle_down(self):
        if self.ycor() > -240:
            new_y = self.ycor() - 20
            self.set_paddle_pos(self.xcor(), new_y)
