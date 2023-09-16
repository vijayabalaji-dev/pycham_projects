from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong_game")
screen.tracer(0)

paddle1 = Paddle()
paddle1.set_paddle_pos(350, 0)

paddle2 = Paddle()
paddle2.set_paddle_pos(-350, 0)

ball = Ball()

score1 = Scoreboard((-200, 270))
score2 = Scoreboard((200, 270))
screen.listen()
screen.onkeypress(paddle1.paddle_up, "Up")
screen.onkeypress(paddle1.paddle_down, "Down")
screen.onkeypress(paddle2.paddle_up, "w")
screen.onkeypress(paddle2.paddle_down, "s")

is_game = True
while is_game:
    time.sleep(0.1)
    screen.update()
    ball.move()


    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(paddle1) < 50 and ball.xcor() > 280 or ball.distance(paddle2) < 50 and ball.xcor() < -280:
        ball.bounce_x()

    if ball.xcor() > 400:
        score1.add_score()
        ball.ball_reset()

    if ball.xcor() < -400:
        score2.add_score()
        ball.ball_reset()

screen.exitonclick()
