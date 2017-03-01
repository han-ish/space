from pygame import display, mixer

scr = display.get_surface()
scrrect = scr.get_rect()

from .score import Score

class Enemi(list,object):
    """This class takes care of the enemy removal"""

    Score.score = 0

    mixer.init()
    sound = mixer.Sound('sound/boom.wav')

    def update(self):
        for f in self[:]:
            f.update()
            if f.shield < 0:
                self.sound.play()
                self.remove(f)
                Score.score += 1
            if f.top > scrrect.bottom:
                self.remove(f)
            else:
                f.render()
        return 0

enemi = Enemi()

