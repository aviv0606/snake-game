from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 16, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.__score = 0
        self.write_score()

    def write_score(self):
        self.goto(0, 270)
        self.color("white")
        self.hideturtle()
        self.penup()
        self.clear()
        self.write(f"Current Score: {self.__score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.__score += 1

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game over.", align=ALIGNMENT, font=FONT)

