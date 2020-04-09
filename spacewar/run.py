from pygame import *
from sqlite3 import connect

scr = display.set_mode((800,600), 0)
scrrect = scr.get_rect()

from spacewar.lib.enemi import enemi
from spacewar.lib.background import Background
from spacewar.lib.ship import ship
from spacewar.lib.shotami import shotami
from spacewar.lib.shotenemi import shotenemi
from spacewar.lib.levelmess import Levelmess

from spacewar.lib.menu import Menu
from spacewar.lib.score import Score

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

        self.level = __import__('spacewar.lib.levels', None, None, [self.levelname])
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

                if ev.type == QUIT or (ev.type == KEYDOWN and ev.key == K_ESCAPE):
                    self.going = False
                    break

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

        print(scoremess)

        highscore = self.store(scoremess)
        Background.render()
        Levelmess.update('score %s High Score : %s' %(scoremess, highscore))
        Levelmess.render()
        display.update()

        if mixer:
            mixer.music.fadeout(1000)

        time.wait(1000)

    def clear(self,level):
        enemi[:] = []
        level.clear()
        ship.clear()

    def store(self,score):
        conn = connect('score.db')
        cursor = conn.cursor()
        try:
            cursor.execute('select * from score_table;')
        except Exception as e:
            return score
        old_score = cursor.fetchone()
        if score > old_score[0]:
            cursor.execute('update score_table set score = %s' %(score))
            conn.commit()
            return score
        return old_score[0]


def main():
    menu = Menu()
    menu.run()
    #Levelmess.update("New Game")
    #Levelmess.render()
    #display.flip()
    game = Game()
    game.run()


if __name__ == '__main__':
    main()
