from graphics import *
from Player import Player
from button import *
from obstacle import *
from time import sleep
from random import randint

#WINDOW
win = GraphWin("GAME", 500, 500)
win.setBackground("light pink")
player_one = Player(50, 50)
player_one.draw(win)

#GAME OVER
game_over = Rectangle(Point(100, 200), Point(400, 400))
game_over.setFill('white')
game_over_text = Text(Point(250, 250), "Game Over! Do You Want To Play Again?")

#YES BUTTON
rect_yes = Rectangle(Point(360, 370), Point(270, 310))
yes_button = Button(rect_yes,"yes")

#NO BUTTON
rect_no = Rectangle(Point(150, 310), Point(240, 370))
no_button = Button(rect_no, "no")

#OBSTACLE STUFF
list = []
running = True
score = 0
score_text = Text(Point(40, 400), f'SCORE: {score}')
score_text.draw(win)




player_one.reset()
while running:
    check = win.checkKey()
    player_one.move(check)
    random_number = randint(1, 100)
    blocks = randint(1, 10)
    sleep(.2)


    for object in list:
        object.move()
        variable = object.get_shape().getP1()
        variable2 = variable.getX()
        if variable2 < 0:
            score += 1
            score_text.setText(f'SCORE: {score}')
            list.remove(object)
            object.undraw()


        if player_one.is_hit(object):
            game_over.draw(win)
            game_over_text.draw(win)
            yes_button.draw(win)
            no_button.draw(win)
            running = False

            exit_clicked = False
            other_clicked = True
            while not exit_clicked:
                point = win.getMouse()
                exit_clicked = no_button.is_clicked(point)
                other_clicked = yes_button.is_clicked(point)
                if exit_clicked:

                    win.close()
                elif other_clicked:

                    game_over.undraw()
                    game_over_text.undraw()
                    yes_button.undraw()
                    no_button.undraw()
                    player_one.reset()
                    for object in list:
                        object.undraw()
                    score_text.setText(f'SCORE: {0}')
        

        if object.is_done():
            list.remove(object)
            object.undraw()


    if blocks == 10:
        object = Obstacle(500, 500)
        list.append(object)
        object.draw(win)








