import time
from turtle import Screen

import shore
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from shore import Shore

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("#85C1E9")

player = Player()
car_manager = CarManager()
score_board = Scoreboard()
shore.Shore()

screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # detection of collision of car with player
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            score_board.game_over()

    # detect successful crossing
    if player.is_at_finis():
        player.go_to_start()
        car_manager.level_up()
        score_board.increase_level()

screen.exitonclick()
