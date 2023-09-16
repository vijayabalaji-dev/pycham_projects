from turtle import Turtle, Screen

screen = Screen()
turtle = Turtle()


def move_forward():
    turtle.forward(10)


def move_backward():
    turtle.backward(10)


def reset():
    turtle.reset()


def clockwise():
    turtle.right(10)


def anti_clockwise():
    turtle.left(10)


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="c", fun=reset)
screen.onkey(key="a", fun=clockwise)
screen.onkey(key="d", fun=anti_clockwise)
screen.exitonclick()
