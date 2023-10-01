from turtle import Turtle
FONT = ("Courier", 14, "normal")
ALIGNMENT = 'center'


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color('black')
        self.penup()
        self.hideturtle()
        self.setposition(-250, 270)
        self.write(arg=f'Level: {self.level}', align=ALIGNMENT, font=FONT)

    def update_scoreboard(self):
        self.clear()
        self.level += 1
        self.write(arg=f'Level: {self.level}', align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.penup()
        self.setposition(0, 0)
        self.write('GAME OVER!', align=ALIGNMENT, font=FONT)
