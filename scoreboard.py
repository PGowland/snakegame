from turtle import Turtle

with open("high_score.txt") as high_score_file:
    high_score_saved = int(high_score_file.read())


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = high_score_saved
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.color("white")
        self.write(f"Score = {self.score}    High Score = {self.high_score}", font=("arial", 20, "bold"),
                   align="center")

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score = {self.score}    High Score = {self.high_score}", font=("arial", 20, "bold"),
                   align="center")

    def game_over(self):
        self.clear()
        self.home()
        self.write("GAME OVER!", font=("arial", 60, "bold"), align="center")
        self.goto(0, -100)
        self.write(f"Your final score was: {self.score}", font=("arial", 20, "bold"), align="center")
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", mode="w") as self.high_score_file:
                self.high_score_file.write(str(self.high_score))

    def update_scoreboard(self):
        self.clear()
        self.goto(0, 260)
        self.score = 0
        self.write(f"Score = {self.score}    High Score = {self.high_score}", font=("arial", 20, "bold"),
                   align="center")
