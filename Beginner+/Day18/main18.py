from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("classic")
timmy.color('red')

screen = Screen()
screen.colormode(255)

def go_to_corner():
    timmy.penup()
    timmy.setx(-420)
    timmy.sety(-340)
    timmy.pendown()

def one_left():
    timmy.penup()
    timmy.left(90)
    timmy.forward(50)
    timmy.left(90)
    timmy.pendown()

def one_right():
    timmy.penup()
    timmy.right(90)
    timmy.forward(50)
    timmy.right(90)
    timmy.pendown()

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    timmy.pencolor(r, g, b)

def make_square():
    for _ in range(4):
        timmy.forward(100)
        timmy.right(90)

def make_dotted_line():
    for _ in range(15):
        timmy.forward(10)
        timmy.penup()
        timmy.forward(10)
        timmy.pendown()

def make_polygon(total_Angles):
    for i in range(3,total_Angles + 1):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        timmy.pencolor(r,g,b)
        for _ in range(i):
            timmy.forward(100)
            timmy.right(360/i)

def random_walk():
    timmy.speed(10)
    timmy.pensize(10)
    angles = (0, 90, 180, 270, 360)
    while True:
        random_color()
        angle = random.choice(angles)
        timmy.forward(30)
        timmy.right(angle)

def make_spirograph():
    timmy.speed('fastest')
    for _ in range(200):
        random_color()
        timmy.circle(100)
        timmy.right(3)

def make_dots(dots_per_line):
        for _ in range(dots_per_line):
            random_color()
            timmy.dot(20)
            timmy.penup()
            timmy.forward(50)
            timmy.pendown()
        timmy.dot(20)


go_to_corner()

def make_art(total_collumns, dots_per_line):
    timmy.speed(0)
    for _ in range(total_collumns):
        make_dots(dots_per_line)
        one_left()
        make_dots(dots_per_line)
        one_right()


make_art(7,16)
screen.exitonclick()