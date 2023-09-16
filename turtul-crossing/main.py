import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
score = Scoreboard()
screen.listen()
screen.onkeypress(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move_car()

    for c in car.cars:
        if player.distance(c) < 30:
            score.game_over()
            game_is_on = False

    if player.is_player_won():
        player.go_to_start()
        car.add_speed()
        score.add_level()


screen.exitonclick()