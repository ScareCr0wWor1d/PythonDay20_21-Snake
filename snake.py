import turtle as t

MOVE_DISTANCE = 20
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]
        self.queue = self.segment[len(self.segment)-1]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_seg(position)

    def add_seg(self, position):
        ti_boute = t.Turtle('square')
        ti_boute.color('green')
        ti_boute.penup()
        ti_boute.goto(position)
        ti_boute.speed('fast')
        self.segment.append(ti_boute)

    def wall_crash(self):
        if (self.head.xcor() <= -300 or self.head.xcor() >= 300
                or self.head.ycor() <= -300 or self.head.ycor() >= 300):
            return False
        else:
            return True

    def moov_f(self):
        for i in range(len(self.segment)-1, 0, -1):
            self.segment[i].goto(self.segment[i-1].xcor(), self.segment[i-1].ycor())
        self.head.forward(MOVE_DISTANCE)
        return self.wall_crash()

    def toorn_l(self):
        self.head.left(90)

    def toorn_r(self):
        self.head.right(90)

    def grow(self):
        self.add_seg(self.segment[-1].position())

    def reset(self):
        for item in self.segment:
            item.goto(1000, 1000)
        self.segment.clear()
        self.create_snake()
        self.head = self.segment[0]