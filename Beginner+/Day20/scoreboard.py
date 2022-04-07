
from turtle import Turtle
ALIGNMENT = 'center'
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        with open('highscore.txt', mode='r') as data:
            self.high_score = int(data.read())
        self.hideturtle()
        self.color("white")
        self.penup()
        self.sety(260)
        self.current_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.current_score} High Score:{self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.current_score += 1
        self.update_scoreboard()

    def restart(self):
        if self.current_score > self.high_score:
            self.high_score = self.current_score
            with open("highscore.txt", mode='w') as data:
                data.write(f'{self.high_score}')
        self.current_score = 0
        self.update_scoreboard()

