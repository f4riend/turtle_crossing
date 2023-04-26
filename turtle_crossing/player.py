from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        self.setheading(90)
        self.shape("turtle")
        self.color("white")
        self.penup()
        self.ready()
    
    
    def move(self):
        self.goto(0,self.ycor() + MOVE_DISTANCE)
    

    def ready(self):
        self.goto(STARTING_POSITION)
    

    def isGameEnd(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
    
