from turtle import Turtle

UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0

class Snake:

    def __init__(self):
        self.a = 0
        self.snake_cords = [(0, 0), (-20, 0), (-40, 0)]
        self.snakes = []
        for i in self.snake_cords:
            self.add_new_snake(i)

    def move(self):
        for current_snake in range(len(self.snakes) - 1, 0, -1):
            x = self.snakes[current_snake - 1].xcor()
            y = self.snakes[current_snake - 1].ycor()
            self.snakes[current_snake].goto(x=x, y=y)
        self.snakes[0].forward(20)

    def add_new_snake(self, i):
        snake = Turtle()
        snake.color("#fff")
        snake.shape("square")
        snake.penup()
        snake.speed("slow")
        snake.goto(i)
        self.snakes.append(snake)

    def extend(self):
        self.add_new_snake(self.snakes[-1].position())

    def up(self):
        if self.snakes[0].heading() != DOWN:
            self.snakes[0].setheading(UP)

    def down(self):
        if self.snakes[0].heading() != UP:
            self.snakes[0].setheading(DOWN)

    def left(self):
        if self.snakes[0].heading() != RIGHT:
            self.snakes[0].setheading(LEFT)

    def right(self):
        if self.snakes[0].heading() != LEFT:
            self.snakes[0].setheading(RIGHT)

    def snake_reset(self):
        for snake in self.snakes:
            snake.goto(1000, 1000)
        self.snakes.clear()
        self.__init__()



