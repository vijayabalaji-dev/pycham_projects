import turtle as t
import random as r
t.colormode(255)
screen = t.Screen()
tur = t.Turtle()

tur.width(7)
tur.shapesize(3)
tur.speed("fastest")
colors = ["red", "green", "yellow", "pink", "blue"]
degrees = [0, 360, 90, 180]
for i in range(200):
    r1 = r.randint(0, 255)
    r2 = r.randint(0, 255)
    r3 = r.randint(0, 255)
    # tur.color(r.choice(colors))
    tur.pencolor((r1, r2, r3))
    tur.forward(20)
    #tur.left(r.choice(degrees))
    tur.setheading(r.choice(degrees))

screen.exitonclick()