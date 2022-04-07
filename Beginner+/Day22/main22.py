import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Making of Screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

# Making our Class Objects
player = Player()
scoreboard = Scoreboard()
cars = CarManager()

# Wait for the player input on 'W'
screen.onkey(player.up, "w")


# Making of the Game
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.move()

    # Checks if player passed Level
    if player.ycor() > 280:
        player.refresh()
        scoreboard.level_increase()
        cars.refresh()
        cars.increase_cars_and_speed()

    # Checks collision with Cars
    for car in cars.cars:
        if player.distance(car) < 22:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()