from turtle import Turtle





class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.color("white")
        self.write(f"Score = {self.score}", font=("arial", 20,  "bold"), align="center")

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score = {self.score}", font=("arial", 20,  "bold"), align="center")

    def game_over(self):
        self.clear()
        self.home()
        self.write("GAME OVER!", font=("arial", 60, "bold"), align="center")
        self.goto(0, -100)
        self.write(f"Your final score was: {self.score}", font=("arial", 20,  "bold"), align="center")

