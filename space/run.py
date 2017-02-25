from pygame import *

scr = display.set_mode((800,600))
scrrect = scr.get_rect()

from lib.enemi import enemi
from lib.background import Background
from lib.ship import ship
from lib.shotami import shotami
from lib.shotenemi import shotenemi
from lib.levelmess import Levelmess

from lib.menu import Menu
from lib.score import Score

#from lib.layer import bulletlayer

#from lib.background import bg  # turning off static methods


class Game(object):
    levels = ['Level1']
    levelcount = 1
    ck0 = time.Clock()
    going = True
    tick = 0

    def run(self):

        self.levelname = self.levels[0]

        self.level = __import__('lib.levels', None, None, [self.levelname])
        self.level = getattr(self.level,self.levelname)

        Game().clear(self.level)

        while self.levels and self.going:
            #levelname = self.levels[0]

            #level = __import__('lib.levels', None, None, [levelname])

            #level = getattr(level,levelname)

            #Game().clear(level)

            display.set_caption('Space Test')

            Levelmess.update('Level {}'.format(self.levelcount))
            #Levelmess.render()
            #display.flip()
            #time.wait(1000)
            while True:
                ev = event.poll()

                if ev.type == QUIT: exit()

                statuslevel = self.level.update()

                #shipstatus = ship.update(ev)

                Background.render()    # trying to remove static methods

                #bg.render()

                #bulletlayer.render()   # turning the bulletlayer off

                shipstatus = ship.update(ev)

                statusmess = Levelmess.render()

                scoremess = Score.update()
                Score.render()


                if shipstatus != None:
                    self.going = False
                    Levelmess.update('GAME OVER')
                    break

                if not statuslevel:
                    self.tick += 1
                    if self.tick >= 250:
                        self.levelcount += 1
                        self.tick = 0
                        break

                if statuslevel == None: # done levels
                    self.going = False
                    break


                shotami.update()
                shotenemi.update()
                enemi.update()

                display.flip()

                self.ck0.tick(50)

            #Levelmess.render()

        Background.render()
        Levelmess.update('Thank you for playing')
        Levelmess.render()
        display.update()

        time.wait(1000)

    def clear(self,level):
        enemi[:] = []
        level.clear()
        ship.clear()



if __name__ == '__main__':
    menu = Menu()
    menu.run()
    #Levelmess.update("New Game")
    #Levelmess.render()
    #display.flip()
    game = Game()
    game.run()



