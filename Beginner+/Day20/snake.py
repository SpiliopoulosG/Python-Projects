from turtle import Turtle

# 4 useful variables for Snake Class
STARTING_POSITIONS = [(0, 0), (-20, 0), (40, 0)]
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

    def __init__(self):
        # Initializes the List and makes a snake ,it also sets the snake head
        self.segment = []
        self.make_snake()
        self.head = self.segment[0]

    def make_snake(self):
        # This Function make the snake and is executed when class is initiated
        for position in STARTING_POSITIONS:
            self.add_Segment(position)

    def add_Segment(self, position):
        new_segment_body = Turtle(shape="square")
        new_segment_body.color('white')
        new_segment_body.penup()
        new_segment_body.goto(position)
        self.segment.append(new_segment_body)

    def extend(self):
        self.add_Segment(self.segment[-1].position())

    def move(self):
        # Make the Snake Move
        for seg_num in range(len(self.segment) - 1, 0, -1):
            # Take the snake's x coordination
            new_x = self.segment[seg_num - 1].xcor()
            # Take the snake's y coordination
            new_y = self.segment[seg_num - 1].ycor()
            self.segment[seg_num].goto(new_x, new_y)
        self.segment[0].forward(20)

    # Make the snake's head go up
    def up(self):
        if self.head.heading() != DOWN:
            self.segment[0].setheading(UP)

    # Make the snake's head go down
    def down(self):
        if self.head.heading() != UP:
            self.segment[0].setheading(DOWN)

    # Make the snake's head go right
    def right(self):
        if self.head.heading() != LEFT:
            self.segment[0].setheading(RIGHT)

    # Make the snake's head go right
    def left(self):
        if self.head.heading() != RIGHT:
            self.segment[0].setheading(LEFT)

    def reset(self):
        for seg in self.segment:
            seg.goto(1000, 1000)
        self.segment.clear()
        self.make_snake()
        self.head = self.segment[0]
