import turtle


class TurtelDraw:

    def draw(self, num, color="black"):
        turtle.color(color)
        for _ in range(num):
            turtle.right(360 / num)
            turtle.forward(100)


screen = turtle.Screen()
# screen.bgcolor("#565667")
turtle = turtle.Turtle()

td = TurtelDraw()
colors = ["red", "green", "yellow", "pink", "blue", "red"]
for i in range(3, 9):
    td.draw(i, colors[i - 3])
# turtle.color("#fff")

# for i in range(0, 4):
#     turtle.forward(100)
#     turtle.left(90)

# for i in range(15):
#     turtle.forward(10)
#     turtle.color("white")
#     turtle.forward(10)
#     turtle.color("black")

# for _ in range(4):
#     turtle.right(360 / 4)
#     turtle.forward(100)
#
# for _ in range(5):
#     turtle.right(360 / 5)
#     turtle.forward(100)
#
# for _ in range(6):
#     turtle.right(360 / 6)
#     turtle.forward(100)
#
# for _ in range(7):
#     turtle.right(360 / 7)
#     turtle.forward(100)
#
# for _ in range(8):
#     turtle.right(360 / 8)
#     turtle.forward(100)

screen.exitonclick()
