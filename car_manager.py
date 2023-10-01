from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple", "violet"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 14)
        if random_chance == 1:
            timmy = Turtle('square')
            timmy.penup()
            timmy.shape('square')
            timmy.color(random.choice(COLORS))
            timmy.shapesize(stretch_wid=1, stretch_len=2)
            timmy.setposition(300, random.randint(-260, 260))
            self.all_cars.append(timmy)

    def car_move(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def inc_speed(self):
        self.car_speed += MOVE_INCREMENT
