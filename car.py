from random import choice,randrange
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Car:
    
    def __init__(self):
        self.allCars = []
        self.speed = STARTING_MOVE_DISTANCE

    def create(self):
        randomChance = randrange(1,6)
        if randomChance == 1:
            brush = Turtle()
            brush.shape("square")
            brush.penup()
            brush.goto(320,randrange(-250,250))
            brush.setheading(180)
            brush.shapesize(stretch_wid=1,stretch_len=2)
            brush.color(choice(COLORS))
            self.allCars.append(brush)

    def move(self):
        for car in self.allCars:
            car.forward(self.speed)
    
    def update(self):
        self.speed += MOVE_INCREMENT