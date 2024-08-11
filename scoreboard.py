from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_sc()

    def update_sc(self):
        self.clear()
        self.write(f"Score:{self.score} High score:{self.high_score}", align="center", font=("Courier", 20, "normal"))


    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_sc()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER", align="center", font=("Courier", 50, "normal"))

    def increase_score(self):
        self.score +=1
        self.update_sc()
