from turtle import Turtle
FONT = ("Courier", 24, "normal")
ALIGNMENT = 'left'


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.current_level = 0
        self.color("Black")
        self.penup()
        self.hideturtle()
        self.goto(-280, 250)
        self.update_scoreboard()

    # Update the Scoreboard
    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.current_level}", align=ALIGNMENT, font=FONT)

    # Increase the level
    def level_increase(self):
        self.current_level += 1
        self.update_scoreboard()

    def game_over(self):
        self.clear()
        self.goto(-85, 0)
        self.write(f"GAME OVER!", align=ALIGNMENT, font=FONT)