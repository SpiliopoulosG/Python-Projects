
from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    # Make the player and place it at the starting line
    def __init__(self):
        super().__init__()
        self.color("green")
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    # Moves the player forward by the moving_distance
    def up(self):
        self.forward(MOVE_DISTANCE)

    # Refreshes the player position to starting line
    def refresh(self):
        self.goto(STARTING_POSITION)

