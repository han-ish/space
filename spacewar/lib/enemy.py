import os

from pygame import display, Rect, image, mask
from math import sin, cos, radians
from random import random, randint, choice

scr = display.get_surface()

SCREENWIDTH = scr.get_width()

from .shotenemi import shotenemi
from .ship import ship

maindir = os.path.dirname(os.path.dirname(__file__))

class Red(Rect,object):
    """The Red enemies"""

    #img = image.load('img/square.png')
    img = image.load(os.path.join(maindir, 'img/square.png'))
    rect = img.get_rect()
    msk = mask.from_surface(img,0)

    class Bullet(Rect,object):

        #img = image.load('img/redbullet.png')
        img = image.load(os.path.join(maindir, 'img/redbullet.png'))
        rect = img.get_rect()
        msk = mask.from_surface(img,0)
        pow = 10

        def __init__(self,midbottom):
            Rect.__init__(self,self.rect)
            self.midbottom = midbottom

        def update(self):
            self.y += 10

        def render(self):
            scr.blit(self.img,self)

    def __init__(self,x,y):
        Rect.__init__(self,Red.img.get_rect(midbottom=(x,y)))
        self.axe = x + 150
        self.X, self.Y = self.midbottom
        self.tau = 0
        self.shield = 1
        self.foo = 0
        self.tick = 0

    def update(self):
        self.tick += 1
        self.tau += 1.8
        self.X = self.axe+sin(radians(self.tau))*300
        self.Y += 0.5
        self.midbottom = self.X, self.Y

        if self.left < ship.centerx < self.right and self.tick >= 10:
            shotenemi.append(Red.Bullet(self.midbottom))
            self.tick = 0


    def render(self):
        if self.foo:
            self.foo -= 1
            scr.blit(Red.img,self)
            return
        scr.blit(Red.img,self)

class SMAlien(Rect,object):
    """The black aliens"""

    #img = image.load('img/space11.png')
    img = image.load(os.path.join(maindir, 'img/space11.png'))
    msk = mask.from_surface(img,1)

    class Bullet(Rect,object):

        #img = image.load('img/oursin.png')
        img = image.load(os.path.join(maindir, 'img/oursin.png'))
        rect = img.get_rect()
        pow = 5

        def __init__(self,midbottom):
            Rect.__init__(self,self.rect)
            self.midbottom = midbottom
            self.dx = random()-0.5
            self.X = self.x
            self.dy = 4+random()
            self.Y = self.y

        def update(self):
            self.Y += self.dy
            self.X += self.dx
            self.x = int(self.X)
            self.y = int(self.Y)

        def render(self):
            scr.blit(self.img,self)

    def __init__(self,x,y):
        Rect.__init__(self,self.img.get_rect(midbottom=(x,y)))
        self.axe = x
        self.X, self.Y = self.midbottom
        self.tau = 0
        self.tick = 0
        self.shield = 1

    def update(self):
        self.tick += 1
        self.tau += 1.8
        self.X = self.axe + sin(radians(self.tau))*300
        self.Y += 0.5
        self.midbottom = self.X, self.Y

        if self.left < ship.centerx < self.right and self.tick >= 10:
            shotenemi.append(self.Bullet(self.midbottom))
            shotenemi.append(self.Bullet(self.midbottom))
            shotenemi.append(self.Bullet(self.midbottom))
            self.tick = 0

    def render(self):
        scr.blit(self.img,self)

