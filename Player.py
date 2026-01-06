from graphics import *


class Player:
    def __init__(self, x_coord, y_coord):
        self.x_coord = x_coord
        self.y_coord = y_coord
        shape_center = Point(x_coord / 2, y_coord / 2)
        shape_radius = y_coord * 0.4
        circle = Circle(shape_center, shape_radius)
        another_circle = Circle(shape_center, shape_radius - 1)
        self.shape = circle
        circle.setFill('light blue')

    def draw(self, win):
        self.shape.draw(win)

    def move(self, direction: str):
        if direction == 'Up':
            self.shape.move(0, -25)
        if direction == 'Down':
            self.shape.move(0, 25)
        if direction == 'Right':
            self.shape.move(25, 0)
        if direction == 'Left':
            self.shape.move(-25, 0)


    def is_hit(self, obstacle):
        player_shape = self.shape
        center = player_shape.getCenter()
        obs = obstacle.get_shape()
        center_distances_x = abs(center.getX() - obs.getCenter().getX())
        center_distances_y = abs(center.getY() - obs.getCenter().getY())
        obs_width = abs(obs.getP1().getX() - obs.getP2().getX())
        obs_height = abs(obs.getP1().getY() - obs.getP2().getY())

        if center_distances_x > (obs_width / 2 + player_shape.getRadius()): return False
        if center_distances_y > (obs_height / 2 + player_shape.getRadius()): return False
        if center_distances_x <= (obs_width / 2): return True
        if center_distances_y <= (obs_height / 2): return True

        corner_distance_sq = ((center_distances_x - obs_width / 2) ** 2) + (center_distances_y - obs_height / 2) ** 2

        return corner_distance_sq <= player_shape.getRadius() ** 2

    def reset(self):
        center_x = 500 / 2
        center_y = 500 / 2
        self.shape.move(center_x - self.shape.getCenter().getX(), center_y - self.shape.getCenter().getY())



