from turtle import Turtle

UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0


class Snake(Turtle):

    def __init__(self):
        super().__init__()
        self.snakes = []
        self.create_snake()
        self.head = self.snakes[0]

    def create_snake(self):
        for snake_index in range(0, 3):
            snake = Turtle("square")
            snake.color("white")
            snake.penup()
            snake.setposition((-20 * snake_index), 0)
            self.snakes.append(snake)

    def move(self):
        for snake_number in range(len(self.snakes) - 1, 0, -1):
            self.snakes[snake_number].goto(self.snakes[snake_number - 1].xcor(), self.snakes[snake_number - 1].ycor())
        self.snakes[0].forward(20)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def extend(self):
        snake = Turtle("square")
        snake.color("white")
        snake.penup()
        snake.setposition((self.snakes[-1].xcor() - 20), self.snakes[-1].ycor())
        self.snakes.append(snake)

    def reset_snake(self):
        for snake in self.snakes:
            snake.goto(-1000, 1000)
        self.snakes.clear()
        self.create_snake()
        self.head = self.snakes[0]
