import time
from turtle import Screen
from player import Player
from scoreboard import Scoreboard
from car_manager import CarManager

player = Player()

screen = Screen()
screen.setup(height=600, width=600)
screen.tracer(0)

screen.listen()
screen.onkey(fun=player.go_up,key="Up")
car_manager=CarManager()

score=Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_car()
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on=False
            score.game_over()

    if player.at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        score.increase_leevel()
        screen.update()

screen.exitonclick()