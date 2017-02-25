from pygame import *

scr = display.set_mode((300,300))
scrrect = scr.get_rect()

from lib.menu import NewGame
from lib.levelmess import Levelmess

def main():
    display.set_caption("Menu Test")
    #background = Surface(scr.get_size())
    #background.fill((255,255,255))
    #scr.blit(background, (0,0))
    new = NewGame()
    new.update()
    Levelmess.update("New Game")

    going = True

    while going:
        ev = event.poll()

        if ev.type == QUIT:
            going = False

        #new.update()
        #new.render()
        Levelmess.render()
        display.flip()

if __name__ == '__main__':
    main()


