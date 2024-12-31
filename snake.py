from turtle import Turtle

DEFAULT_SNAKE_STEP = 20
DEFAULT_SNAKE_SIZE = 7

RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270
class Snake:

    def __init__(self):
        self.body = []
        self.initialize_snake()
        self.head = self.body[0]

    def create_snake_body_part(self, x, y):
        snake_part = Turtle()
        snake_part.shape("turtle")
        snake_part.color("white")
        snake_part.penup()
        snake_part.goto(x, y)
        self.body.append(snake_part)

    def initialize_snake(self):
        initial_x_co_ordinate = 0
        initial_y_co_ordinate = 0
        for self.body_index in range(0, DEFAULT_SNAKE_SIZE):
            self.create_snake_body_part(initial_x_co_ordinate, initial_y_co_ordinate)
            initial_x_co_ordinate -= DEFAULT_SNAKE_STEP

    def move(self):
        for body_part_index in range(len(self.body) - 1, 0, -1):
            x = self.body[body_part_index - 1].xcor()
            y = self.body[body_part_index - 1].ycor()
            self.body[body_part_index].goto(x, y)
        self.head.forward(DEFAULT_SNAKE_STEP)

    def is_valid_direction(self, angle):
        angle_difference = self.head.heading() - angle
        if angle_difference == 180 or angle_difference == -180:
            return False
        return True

    def left(self):
        if self.is_valid_direction(LEFT):
            self.head.setheading(LEFT)

    def right(self):
        if self.is_valid_direction(RIGHT):
            self.head.setheading(RIGHT)

    def up(self):
        if self.is_valid_direction(UP):
            self.head.setheading(UP)

    def down(self):
        if self.is_valid_direction(DOWN):
            self.head.setheading(DOWN)

    def grow(self):
        tail = self.body[len(self.body) - 1]
        self.create_snake_body_part(tail.xcor(), tail.ycor())
