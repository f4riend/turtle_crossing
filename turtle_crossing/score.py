from turtle import Turtle
FONT = ("Courier", 12, "normal")


class Score(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(-250,270)
        self.write(f"LEVEL: {self.score}",align="center",font=FONT)

    def update(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}",align="center",font=FONT)
    

    def gameOver(self):
        self.home()
        self.write("Game Over",align="center",font=FONT)
    
    def gameOverClear(self):
        self.clear()
