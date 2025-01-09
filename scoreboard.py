from turtle import Turtle

class Scoreboard:
    def __init__(self):
        self.level = 1
        self.board = Turtle()
        self.board.hideturtle()
        self.board.penup()
        self.board.goto(-280, 260)
        self.board.color("black")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.board.clear()
        self.board.write(f"Level: {self.level}", align="left", font=("Courier", 16, "normal"))

    def game_over(self):
        self.board.goto(0,0)
        self.board.write("Game Over", align="center", font=("Courier", 16, "normal"))



    def increase_level(self):
        self.level += 1
        self.update_scoreboard()
