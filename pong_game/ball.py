from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("#fff")
        self.shape("circle")
        self.penup()
        self.x = 10
        self.y = 10

    def move(self):
        x = self.xcor() + self.x
        y = self.ycor() + self.y
        self.goto(x, y)

    def bounce_y(self):
        self.y *= -1

    def bounce_x(self):
        self.x *= -1

    def ball_reset(self):
        self.goto(0, 0)
        self.bounce_x()
