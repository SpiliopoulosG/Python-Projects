import turtle
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(20)

def move_backward():
    tim.backward(20)

def go_right():
    tim.right(10)

def go_left():
    tim.left(10)

def clear():
    tim.clear()
    tim.penup()
    tim.setx(0)
    tim.sety(0)
    tim.setheading(0)
    tim.pendown()


screen.listen()
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="a", fun=go_left)
screen.onkey(key="d", fun=go_right)
screen.onkey(key="c", fun=clear)


screen.exitonclick()