from turtle import Turtle


ALIGNMENT = 'center'
FONT = ('Courier', 80, "normal")


class Scoreboard(Turtle):

    #Creates The Scoreboard
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.current_speed = 0
        self.update_scoreboard()


    # Updates the Score for both players
    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(self.r_score, align=ALIGNMENT, font=FONT)

    # Adds a score point to the left player
    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    # Adds a score point to the right player
    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()


