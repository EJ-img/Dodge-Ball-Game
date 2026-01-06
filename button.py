from graphics import *

class Button():

    def __init__(self, shape, label):
        self.shape = shape
        self.text = Text(shape.getCenter(), label)

    def draw(self, win: GraphWin):
        self.shape.draw(win)
        self.text.draw(win)

    def undraw(self):
        self.shape.undraw()
        self.text.undraw()

    def is_clicked(self, point: Point):
        center = self.shape.getCenter()
        width = abs(self.shape.getP1().x - self.shape.getP2().x)
        height = abs(self.shape.getP1().y - self.shape.getP2().y)
        y_top = center.y + height / 2
        y_bottom = center.y - height / 2
        x_left = center.x - width / 2
        x_right = center.x + width / 2

        x_point = point.getX()
        y_point = point.getY()

        res = x_left <= x_point <= x_right and y_bottom <= y_point <= y_top
        return res