import turtle as t
from main import colors_list
import random as r


def draw():
    for i in range(10):

        turtle.dot(20, r.choice(colors_list))
        if i < 9:
            turtle.fd(50)

def left():
    turtle.penup()
    turtle.left(90)
    turtle.fd(50)
    turtle.left(90)


def right():

    turtle.right(90)
    turtle.fd(50)
    turtle.right(90)


t.colormode(255)
screen = t.Screen()
turtle = t.Turtle()
turtle.speed("fastest")
turtle.color("#fff")
turtle.penup()
turtle.hideturtle()
TURTLE_SIZE = 20
turtle.goto(TURTLE_SIZE / 2 - screen.window_width() / 2, screen.window_height() / 2 - TURTLE_SIZE / 2)

for i in range(1,11):
    draw()
    if i % 2 == 0:
        left()
    else:
        right()
# turtle.pendown()
screen.exitonclick()
