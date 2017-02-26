
from pygame import time
from random import randint
from .enemy  import Red, SMAlien
from .enemi import enemi


class Level1(object):
    """STAGE 1"""

    @staticmethod
    def v1():
        if Level1.count1:
            Level1.t1 += 1
            if Level1.t1 == 75:
                r = SMAlien(randint(100+200,300+200),0)

                #r = Red(randint(100,300),0)

                enemi.append(r)
                Level1.count1 -= 1
                Level1.t1 = 0
            return 1
        else:
            Level1.t1 = 0
            Level1.v.pop(0)
            return 0


    @staticmethod
    def v2():
        if Level1.count2:
            Level1.t1 += 1
            if Level1.t1 == 75:
                r = Red(randint(100+200,300+200),0)
                enemi.append(r)
                Level1.count2 -= 1
                Level1.t1 = 0
            return 1
        else:
            Level1.t1 = 0
            Level1.v.pop(0)
            return 0

    @staticmethod
    def wait():
        if not enemi:
            Level1.t1 += 1
            if Level1.t1 == 250:
                Level1.t1 = 0
                Level1.v.pop(0)
            return 0
        return 1


    #v       = [v1,wait,v2,wait]
    #v = [v1,v2]

    @staticmethod
    def update():
        if Level1.v:
            val = Level1.v[0]()
            #print bool(val)
            return bool(val)
        #return bool(Level1.v)
            #return bool(val)

    @staticmethod
    def clear():
        #Level1.v = [Level1.v1,Level1.wait,Level1.v2,Level1.wait]
        Level1.v = [Level1.v1,Level1.wait,Level1.v2,Level1.wait]
        Level1.count1  = 8
        Level1.count2  = 8
        Level1.t1      = 0
        Level1.tick = 0
