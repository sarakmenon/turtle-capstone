import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_up, "Up")

level = 1

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()


    if car_manager.check_collision(player):
        player.color("red")
        game_is_on = False
        scoreboard.game_over()

    if player.ycor() >= 290:
        scoreboard.increase_level()
        scoreboard.update_scoreboard()
        car_manager.increase_speed()
        player.sety(-290)


screen.exitonclick()
