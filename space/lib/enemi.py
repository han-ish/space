from pygame import display

scr = display.get_surface()
scrrect = scr.get_rect()

from .score import Score

class Enemi(list,object):

    Score.score = 0

    def update(self):
        for f in self[:]:
            f.update()
            if f.shield < 0:
                self.remove(f)
                Score.score += 1
            if f.top > scrrect.bottom:
                self.remove(f)
            else:
                f.render()
        return 0

enemi = Enemi()

