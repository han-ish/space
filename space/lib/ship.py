#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame         import image,Rect,mask,key,font,draw,Color,transform,surfarray
from pygame         import gfxdraw
from pygame.locals  import *
from pygame         import display
scr = display.get_surface()
scrrect = scr.get_rect()

from .shotami import shotami


class DoubleLazer(object):

    cadence = 10
    temp = 0

    class Bullet(Rect,object):
        img = image.load('img/lazer1.png')
        msk = mask.from_surface(img,1)
        rect = img.get_rect()
        pow = 10

        def __init__(self,pos):
            Rect.__init__(self,self.rect)
            self.midbottom = pos

        def update(self):
            self.y -= 10
            #self.pos = self.x, self.y

        def render(self):
            scr.blit(self.img,self)

    def __init__(self,get_pos1,get_pos2):
        self.get_pos1 = get_pos1
        self.get_pos2 = get_pos2

    def shot(self):
        if DoubleLazer.temp > DoubleLazer.cadence:
            shotami.append(DoubleLazer.Bullet(self.get_pos1()))
            shotami.append(DoubleLazer.Bullet(self.get_pos2()))
            DoubleLazer.temp = 0

    def update(self):

        DoubleLazer.temp += 1


class Ship(Rect,object):

    img          = image.load('img/xwing.png')
    rect         = img.get_rect()
    img2         = image.load('img/xwing2.png')
    msk          = mask.from_surface(img,1)
    lazertempfx  = image.load('img/lazertemp.png')
    shield = 1
    alive = True


    def __init__(self):
        self.dirx = 1
        self.diry = 0
        self.X, self.Y = 600, 600

        self.memgun1accum    = 3
        self.memshieldmax    = 100.
        self.memshield_      = 50
        self.memsettingbonus = 10
        self.memloader1 = 1
        self.shotbutton = False
        Rect.__init__(self,self.rect)
        self.lazer = DoubleLazer(lambda : self.midleft,lambda : self.midright)
        #self.clear()
        #self.midbottom = 300, 600

    def gun_update(self):

        self.lazer.update()
        if self.shotbutton:
            self.lazer.shot()


    def update(self,ev):
        if ev.type == KEYDOWN:
            self.dirx += (ev.key == K_RIGHT) - (ev.key == K_LEFT)
            self.diry +=  (ev.key == K_DOWN) - (ev.key == K_UP)
            if ev.key == K_SPACE:
                self.shotbutton = True
            if ev.key == K_F1 and self.loader1:
                if self.lancetorpille.shot(torpedo1):
                    self.loader1 -= 1
        elif ev.type == KEYUP:
            #self.dirx += (ev.key == K_LEFT) - (ev.key == K_RIGHT)
            #self.diry +=   (ev.key == K_UP) - (ev.key == K_DOWN)
            if ev.key == K_SPACE:
                self.shotbutton = False

        #print "self.dirx : ",self.dirx, "self.diry : ",self.diry

        self.X += self.dirx
        self.Y += self.diry

        if self.X < 0 + 20:
            self.X = 20
        elif self.X > 800 - 20:
            self.X = 780
        if self.Y < 0 + 20:
            self.Y = 20
        elif self.Y > 600 - 20:
            self.Y = 580

        self.midbottom = self.X, self.Y

        self.gun_update()

        if self.shield < 0:
            return 0

        scr.blit(self.img,ship)

    #def gun_update():
    #    self.lazer.update()
    #    if self.shotbutton:
    #        self.lazer.shot()


    def clear(self):
        #self.size           = self.rect.size
        #self.midbottom      = (200,490)
        #self.acc            = 0.5
        #self.vmax           = 3
        #self.vitx           = 0
        #self.vity           = 0
        #k = key.get_pressed()
        #self.dirx           = k[K_RIGHT]-k[K_LEFT]
        #self.diry           = k[K_DOWN]-k[K_UP]
        pass
ship = Ship()



