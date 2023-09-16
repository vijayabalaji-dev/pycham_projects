from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(width=500, height=400)
user_input = screen.textinput(title="Make a Bet", prompt="Enter the turtle colour you bet?")

rainbow = ["red", "green", "blue", "yellow", "orange", "indigo", "violet"]
y_cord = [150, 100, 50, 0, -50, -100, -150]
turtles = []
for i in range(7):
    tim = Turtle("turtle")
    tim.penup()
    tim.speed("fastest")
    tim.color(rainbow[i])
    tim.goto(x=-230, y=y_cord[i])
    turtles.append(tim)

is_race_on = False

if user_input:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            if user_input == turtle.pencolor():
                print(f"You won the race wining colour is {turtle.pencolor()}")
            else:
                print(f"You lose the wining colour is {turtle.pencolor()}")

        move = randint(0, 10)
        turtle.forward(move)

screen.exitonclick()
