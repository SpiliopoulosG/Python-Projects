
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Starts the game
game_is_on = True
# Make the Snake
snake = Snake()
food=Food()
score=Scoreboard()

# Make the Screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# Make Screen Listen to our Keys
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


while game_is_on:
    screen.update()
    time.sleep(0.1)
    # Keeps the Snake Moving
    snake.move()

    # Detects Collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase_score()
        snake.extend()

    # Detect Collision with Wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.restart()
        snake.reset()


    # Detect Collision with Tail
    for segment in snake.segment[1:]:

        if snake.head.distance(segment) < 10:
            score.restart()
            snake.reset()


# Exits the screen when click on 'x'
screen.exitonclick()