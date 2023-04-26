from time import sleep
from turtle import Screen
from player import Player
from car import Car
from score import Score

canvas = Screen()
canvas.bgcolor("black")
canvas.setup(width=600, height=600)
canvas.tracer(0)


player = Player()
score = Score()
cars = Car()


canvas.listen()
canvas.onkey(player.move,"Up")


isGameOn = True
while isGameOn:
    sleep(0.1)
    canvas.update()

    cars.create()
    cars.move()

    for car in cars.allCars:
        if player.distance(car) < 20:
            isGameOn = False
            score.gameOver()
    
    if player.isGameEnd():
        player.ready()
        cars.update()
        score.update()


canvas.exitonclick()
