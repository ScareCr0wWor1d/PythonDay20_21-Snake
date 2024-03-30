from turtle import Turtle
FONT = ('Courier', 30, 'italic')
FONTGO = ('Arial', 60, 'bold')
ALIGN = 'center'

class Scoreboard(Turtle):

    def __init__(self):
        self.pointage = 0
        super().__init__()
        self.color()
        self.color('blue')
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.updatesb()

    def updatesb(self):
        self.write(f"Score: {self.pointage}", font=FONT, align=ALIGN)

    def game_over(self):
        self.goto(0, 0)
        self.color('red')
        self.write("Game Over", font=FONTGO, align='center')

    def addpts(self):
        self.pointage += 1
        self.clear()
        self.updatesb()

