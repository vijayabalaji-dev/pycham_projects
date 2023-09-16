import turtle as t
import random as ra

t.colormode(255)

screen = t.Screen()
tur = t.Turtle()
tur.width(2)
tur.speed("fastest")
r = 100

for i in range(int(360/5)):
    r1 = ra.randint(0, 255)
    r2 = ra.randint(0, 255)
    r3 = ra.randint(0, 255)
    tur.pencolor((r1, r2, r3))
    tur.circle(r)
    tur.left(5)


screen.exitonclick()