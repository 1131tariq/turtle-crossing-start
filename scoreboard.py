from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto(-220, 260)
        self.score = 1
        self.print_score()

    def increase_score(self):
        self.score += 1

    def print_score(self):
        self.clear()
        self.pendown()
        self.write(arg=f"Level: {self.score}", align="center", font=FONT)

    def gameover(self):
        self.goto(0,0)
        self.pendown()
        self.write(arg="Game Over", align="center", font=FONT)



