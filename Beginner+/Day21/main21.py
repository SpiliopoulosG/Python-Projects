from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# The creation of our Paddles
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

# Making the Screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My Classic Pong Game")
screen.listen()
screen.tracer(0)


# Player 1 Control(Right Puddle)
screen.onkey(r_paddle.up, 'Up')
screen.onkey(r_paddle.down, 'Down')

# Player 2 Control(Left Puddle)
screen.onkey(l_paddle.up, 'w')
screen.onkey(l_paddle.down, 's')

# Our Game Code
game_is_on = True

while game_is_on:
    time.sleep(ball.movement_speed)
    screen.update()
    ball.move()

    # Detect Collision with top or bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:

        ball.bounce()

    # Detect Collision with Paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:

        ball.bounce_x()

    # Detect if goooooooooooalllllllllll
    if ball.xcor() > 380:
        ball.refresh()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.refresh()
        scoreboard.r_point()


screen.exitonclick()