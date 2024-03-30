from turtle import Turtle
from random import randint


class Bouffe(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('circle')
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('orange')
        self.speed('fastest')
        self.move_bouffe()

    def move_bouffe(self):
        randx = randint(-280, 280)
        randy = randint(-280, 280)
        self.goto(randx, randy)
