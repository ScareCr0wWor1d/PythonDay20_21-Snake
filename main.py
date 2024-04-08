import time
import turtle as t
from tkinter import messagebox
from time import sleep

import scoreboard
import snake
import bouffe

pointage = 0


def toorn_l():
    segment[0].left(90)


def toorn_r():
    segment[0].right(90)


my_scrn = t.Screen()
my_scrn.setup(600, 600)
my_scrn.bgcolor('black')
my_scrn.title("Snaaaaaake... It's a Snake!!!!")
my_scrn.tracer(0)

my_snk = snake.Snake()
manger = bouffe.Bouffe()
score = scoreboard.Scoreboard()

my_scrn.update()

pasfin = True

t.listen()

t.onkeypress(my_snk.toorn_l, 'Left')
t.onkeypress(my_snk.toorn_r, 'Right')

while pasfin:
    my_scrn.update()
    sleep(0.09)
    pasfin = my_snk.moov_f()
    if my_snk.head.distance(manger) <= 15:
        manger.move_bouffe()
        score.addpts()
        my_snk.grow()

    for segment in my_snk.segment[1:]:
        if my_snk.head.distance(segment) < 10:
            pasfin = False

    if not pasfin:
        score.reset()
        if messagebox.askyesno('Continue', "Voulez-vous continuer?"):
            my_snk.reset()
            pasfin = True
            time.sleep(1)

my_scrn.exitonclick()
