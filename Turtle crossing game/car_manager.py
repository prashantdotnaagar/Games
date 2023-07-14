from turtle import Turtle
import random
COLORS = ['red', 'green', 'blue', 'orange','yellow', 'purple']
MOVE_INCREMENT= 10
STARTING_MOVE_DISTANCE=5


class CarManager:

    def __init__(self):
        self.all_cars=[]
        self.car_speed=MOVE_INCREMENT

    def create_car(self):
        random_number = random.randint(1, 6)
        if random_number == 1:
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1,stretch_len=2)
            new_car.penup()
            random_y=random.randint(-230,230)
            new_car.goto(300,random_y)
            self.all_cars.append(new_car)

    def move_car(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed+= MOVE_INCREMENT
