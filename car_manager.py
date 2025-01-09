import random
from turtle import Turtle
import time

COLORS = ["CadetBlue2", "aquamarine", "BlueViolet", "brown2", "coral2", "darkmagenta", "cyan3", "DarkOrchid", "DarkTurquoise", "DeepPink", "DeepPink4", "DeepSkyBlue2", "hotpink", "indianred", "maroon", "midnightblue", "PaleVioletRed", "pink2", "plum1", "PowderBlue", "orchid", "PaleTurquoise1", "RoyalBlue1", "salmon", "SkyBlue", "SlateBlue1", "SteelBlue1", "turquoise1", "VioletRed", "RosyBrown1"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    def __init__(self):
        self.cars = []
        self.move_distance = STARTING_MOVE_DISTANCE

    def create_car(self):
        """Create a car at a random y-position and random color."""
        if random.random() < .35:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)  # Make it more rectangular like a car
            new_car.color(random.choice(COLORS))
            new_car.penup()
            # Randomly place the car along the y-axis at the right edge of the screen
            new_car.setposition(300, random.randint(-250, 250))
            self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.setx(car.xcor() - self.move_distance)

    def increase_speed(self):
        self.move_distance += MOVE_INCREMENT

    def check_collision(self, player_turtle):
        for car in self.cars:
            if player_turtle.distance(car) < 10:
                return True
        return False
