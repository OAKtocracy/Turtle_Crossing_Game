import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("white")

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()


screen.listen()
screen.onkey(fun=player.move, key='Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.car_move()
    car_manager.create_car()

    if player.ycor() >= 290:
        player.setposition(0, -280)
        scoreboard.update_scoreboard()
        car_manager.inc_speed()

    for car in car_manager.all_cars:
        if car.distance(player) < 22:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
