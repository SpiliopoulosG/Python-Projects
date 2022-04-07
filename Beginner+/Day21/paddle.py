from turtle import Turtle


class Paddle(Turtle):

    # Creates the Puddles
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.showturtle()
        self.setposition(position)

    # It moves the puddle up
    def up(self):
        new_y = self.ycor() + 50
        self.sety(new_y)

    # It moves the puddle down
    def down(self):
        new_y = self.ycor() - 50
        self.sety(new_y)
