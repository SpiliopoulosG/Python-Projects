import turtle
from turtle import Turtle,Screen
import random


is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race?Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
tortoises = []

def make_turtles(total_turtles = colors):
        for i in total_turtles:
            i = Turtle(shape="turtle")
            tortoises.append(i)

def place_turtles():
        h =-100
        i = 0
        for turtle in tortoises:
            turtle.color(colors[i])
            turtle.penup()
            turtle.goto(x=-230, y=h)
            h += 50
            i += 1

make_turtles()
place_turtles()
if user_bet:
    is_race_on = True
#Starting Game
while is_race_on:

        for turtle in tortoises:
            if turtle.xcor() > 230:
                is_race_on = False
                winning_color = turtle.pencolor()
                if winning_color == user_bet:
                    print(f"You've won! The {winning_color} turtle is the winner!")
                else:
                    print(f"You've lost! The {winning_color} turtle is the winner!")

            rand_distance = random.randint(0, 10)
            turtle.forward(rand_distance)


screen.exitonclick()