from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Arial', 14, 'normal')
TEXT_POSITION = (0, 260)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.points = 0
        self.penup()
        self.goto(TEXT_POSITION)
        self.hideturtle()
        self.color("white")
        self.speed("fastest")
        self.clear()
        self.score()

    def score(self):
        self.write(f"Score: {self.points}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.clear()
        self.points += 1

    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)
