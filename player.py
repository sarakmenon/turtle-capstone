from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.setheading(90)
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.goto(STARTING_POSITION)

    def move_up(self):
        self.sety(self.ycor() + MOVE_DISTANCE)
