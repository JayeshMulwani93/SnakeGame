from turtle import Turtle

from snake import Snake
from food import Food
import time

FONT_STYLE = "Verdana"
FONT_TYPE = "normal"
ALIGNMENT = "CENTER"
FONT_SIZE = 15

class SnakeGame:
    def __init__(self):
        self.snake = Snake()
        self.food = Food()
        self.pen = Turtle()
        self.initialize_pen()
        self.score = 0
        with open("resources/data.txt", mode="r") as file:
            contents = file.readline()
            if len(contents) == 0:
                self.high_score = 0
            else:
                self.high_score = int(contents)

    def initialize_pen(self):
        self.pen.color("white")
        self.pen.hideturtle()
        self.pen.goto(0, 180)
        self.pen.penup()

    def play_game(self):
        food_co_ordinates = self.food.get_food_co_ordinates()
        if self.has_snake_eaten_food(food_co_ordinates[0], food_co_ordinates[1]):
            self.food.regenerate()
            self.snake.grow()
        self.snake.move()
        time.sleep(0.1)

    def has_snake_eaten_food(self, x, y):
        x_snake = self.snake.head.xcor()
        y_snake = self.snake.head.ycor()
        if abs(x_snake - x) <= 10 and abs(y_snake - y) <= 10:
            self.score += 1
            return True
        return False

    def has_collision_occurred(self, screen_dimensions_x, screen_dimensions_y):
        snake_head_x = self.snake.head.xcor()
        snake_head_y = self.snake.head.ycor()

        if snake_head_x <= -screen_dimensions_x/2 or snake_head_x >= screen_dimensions_x/2:
            return True

        if snake_head_y <= -screen_dimensions_y / 2 or snake_head_y >= screen_dimensions_y / 2:
            return True

        # 1: below is slicing concept!
        for body_part in self.snake.body[1:]:
            # if self.snake.head == body_part:
            #     pass
            if self.snake.head.distance(body_part) < 10:
                return True

        return False

    def display_score(self):
        self.pen.clear()
        self.pen.write(arg=f"Score = {str(self.score)}, High score is {str(self.high_score)}", align=ALIGNMENT, font=(FONT_STYLE, FONT_SIZE, FONT_TYPE))

    def game_over(self):
        self.pen.goto(0, 0)
        if self.score > self.high_score:
            with open("resources/data.txt", mode="w") as file:
                file.writelines(str(self.score))
            self.pen.write(arg=f"Game Over, You've set the high score of {self.score}!", align=ALIGNMENT, font=(FONT_STYLE, FONT_SIZE, FONT_TYPE))
        else:
            self.pen.write(arg="Game Over!", align=ALIGNMENT, font=(FONT_STYLE, FONT_SIZE, FONT_TYPE))