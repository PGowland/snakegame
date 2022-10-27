from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()

screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
screen.onkey(snake.down, "Down")
screen.onkey(snake.up, "Up")

screen.update()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    snake.move()
    screen.update()
    for segment in range(1, len(snake.snakes) - 1):
        if snake.snakes[segment].distance(snake.head) < 5:
            scoreboard.game_over()
            time.sleep(2)
            snake.reset_snake()
            scoreboard.update_scoreboard()

    if food.distance(snake.head) < 15:
        food.new_locale()
        snake.extend()
        scoreboard.increase_score()
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.game_over()
        time.sleep(2)
        snake.reset_snake()
        scoreboard.update_scoreboard()

screen.exitonclick()
