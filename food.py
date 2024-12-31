from turtle import Turtle
import random

class Food:

    def __init__(self):
        self.item = Turtle()
        self.item.shape("circle")
        self.item.penup()
        self.item.color("blue")
        self.regenerate()

    def get_food_co_ordinates(self):
        x = self.item.xcor()
        y = self.item.ycor()
        return x, y

    def regenerate(self):
        self.item.goto(random.randint(-240, 240), random.randint(-190, 190))

