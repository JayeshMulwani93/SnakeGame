from turtle import Screen
from game import SnakeGame

SCREEN_DIMENSIONS = [500, 400]

screen = Screen()
screen.setup(width=SCREEN_DIMENSIONS[0], height=SCREEN_DIMENSIONS[1])

screen.tracer(0)
screen.bgcolor("black")
game = SnakeGame()
screen.update()
screen.listen()

screen.onkeypress(key = "Up", fun=game.snake.up)
screen.onkeypress(key = "Left", fun=game.snake.left)
screen.onkeypress(key = "Right", fun=game.snake.right)
screen.onkeypress(key = "Down", fun=game.snake.down)

while not game.has_collision_occurred(SCREEN_DIMENSIONS[0], SCREEN_DIMENSIONS[1]):
    game.display_score()
    game.play_game()
    screen.update()

game.game_over()
screen.update()
screen.exitonclick()