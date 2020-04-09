import os

from pygame import display,font

scr = display.get_surface()
scrrect = scr.get_rect()

font.init()
print("path: ", __file__)
imgdir = os.path.dirname(os.path.dirname(__file__))
#police = font.Font('Roboto.ttf', 40)
police = font.Font(os.path.join(imgdir, 'Roboto.ttf'), 40)

class Score(object):

    score = 0

    @staticmethod
    def update():
        Score.mess = police.render("Score : " + str(Score.score), 1, (200,200,200))
        return Score.score
    @staticmethod
    def render():
        scr.blit(Score.mess, (0,0))
