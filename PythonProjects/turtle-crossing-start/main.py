import time
from turtle import Screen

import car_manager
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.title('Turtle Crossing Game')
screen.setup(width=600, height=600)
screen.tracer(0)

car_manager = CarManager()
player = Player()
score = Scoreboard()

screen.listen()
screen.onkey(player.move_up, 'Up')

game_is_on = True
while game_is_on:
    time.sleep(car_manager.move_speed)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    for cars in car_manager.all_cars:
        if cars.distance(player) < 20:
            game_is_on = False
            score.game_over()

    if player.is_at_finish_line():
        score.increase_level()
        player.reset_position()
        car_manager.level_up()

screen.exitonclick()












