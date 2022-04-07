from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.CAR_DIFFICULTY = 0
        self.CAR_SPEED = 0
        self.penup()
        self.hideturtle()
        self.cars = []
        for i in range(30 + self.CAR_DIFFICULTY):
            self.add_car()

    def add_car(self):

        new_car = Turtle(shape="square")
        new_car.color(random.choice(COLORS))
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.penup()
        new_car.goto(random.randint(100, 1000), random.randint(-230, 250))
        new_car.setheading(180)
        self.cars.append(new_car)

    def move(self):

        for self.car in self.cars:
            if self.car.xcor() < -300:
                self.car.hideturtle()
                self.car.goto(random.randint(250, 1000), random.randint(-230, 250))
                self.car.showturtle()
            else:
                self.car.forward(random.randint(0, MOVE_INCREMENT + self.CAR_SPEED))

    def refresh(self):
        for self.car in self.cars:
            self.car.hideturtle()
            self.car.goto(random.randint(100, 1000), random.randint(-230, 250))
            self.car.showturtle()

    def increase_cars_and_speed(self):
        self.CAR_DIFFICULTY += 1
        self.CAR_SPEED += 1
