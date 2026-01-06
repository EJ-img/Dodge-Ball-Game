from graphics import *
from random import randint, uniform
from time import sleep


class Obstacle():
    def __init__(self, x_coord, y_coord):
        random_width = randint(x_coord * .05, x_coord * .10)
        random_height = randint(y_coord * .05, y_coord * .10)
        random_variable = randint(1, y_coord)
        x1 = x_coord
        y1 = random_variable
        x2 = x1 + random_width
        y2 = y1 + random_height
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.shape = Rectangle(Point(x1, y1), Point(x2,y2))
        list_colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink']
        color_position = randint(0, 6)
        self.shape.setFill(list_colors[color_position])
        self.speed = uniform(x_coord * .05, x_coord * .08)

    def draw(self, win):
        self.shape.draw(win)

    def undraw(self):
        self.shape.undraw()

    def get_random(move_amount: int):
        movement = randint(-move_amount, move_amount)
        return movement

    def move(self):
        self.shape.move(self.speed * -1, 0)

    def is_done(self):
        if self.x_coord <= 0:
            return True

    def get_shape(self):
        return self.shape


