from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time


# screen has a method called trace which can be used to turn on and off animations
# once tracer(0) is set to 0 animations will be offed
# to update the screen we should call screen.update method manually every to update the screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("#000")
screen.title("Snake Pong")
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.2)
    snake.move()

    if snake.snakes[0].distance(food) < 15:
        food.refresh()
        score.add_score()
        snake.extend()

    # collision with wall

    if (snake.snakes[0].xcor() > 280 or snake.snakes[0].xcor() < -280
            or snake.snakes[0].ycor() > 280 or snake.snakes[0].ycor() < -280):
        score.reset_score()
        snake.snake_reset()

    # collision with tail

    for s in snake.snakes:
        if s == snake.snakes[0]:
            pass
        elif snake.snakes[0].distance(s) < 10:
            score.reset_score()
            snake.snake_reset()

screen.exitonclick()
