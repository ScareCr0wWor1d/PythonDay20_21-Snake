from turtle import Turtle

FONT = ('Courier', 20, 'italic')
FONTGO = ('Arial', 60, 'bold')
ALIGN = 'center'


class Scoreboard(Turtle):

    def __init__(self):
        self.pointage = 0
        with open("HS.txt") as file:
            self.highscore = int(file.read())
        super().__init__()
        self.color('blue')
        self.hideturtle()
        self.penup()
        self.updatesb()

    def updatesb(self):
        self.clear()
        self.goto(-100, 260)
        self.write(f"Score: {self.pointage}", font=FONT, align=ALIGN)
        self.goto(100, 260)
        self.write(f"HighScore: {self.highscore}", font=FONT, align=ALIGN)

    def reset(self):
        if self.pointage > self.highscore:
            self.highscore = self.pointage
            with open("HS.txt", 'w') as file:
                file.write(str(self.highscore))
        self.pointage = 0
        self.updatesb()

#    def game_over(self):
#        self.goto(0, 0)
#        self.color('red')
#        self.write("Game Over", font=FONTGO, align='center')
#        self.highscore = self.pointage

    def addpts(self):
        self.pointage += 1
        self.clear()
        self.updatesb()

