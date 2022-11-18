import turtle
from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.write(f"Score is {self.score}", align="center", font=("Arial", 20, "normal"))

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score is {self.score}", align="center", font=("Arial", 20, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over!", align="center", font=("Arial", 24, "normal"))
        a = turtle.textinput("Game Over", "Do you want to play again? Enter 'yes' or 'no'")
        if a == 'yes':
            return True
        else:
            return False
