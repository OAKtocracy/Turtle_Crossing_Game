from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 295


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setposition(STARTING_POSITION)
        self.shape('turtle')
        self.color("black")
        self.setheading(90)

    def move(self):
        new_y = self.ycor() + MOVE_DISTANCE
        if new_y < FINISH_LINE_Y:
            self.setposition(0, new_y)

