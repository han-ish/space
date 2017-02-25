import pygame
from pygame.locals import *

GREEN = (0, 255, 0)
RED = (255, 0, 0)


class Mouse(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #self.image = pygame.Surface([40,40])
        #self.image.fill(GREEN)
        #self.rect = self.image.get_rect()
        self.rect = pygame.rect.Rect((0,0),(0,0))

    def update(self):

        pos = pygame.mouse.get_pos()
        #self.rect.midtop = pos
        #print dir(pos)

    def clicked(self,new):

        #hitbox = self.rect.inflate(-5,-5)
        return hitbox.colliderect(new.rect)


class New(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([60,40])
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = 120
        self.rect.y = 20
        self.font = pygame.font.Font(None, 36)
        self.text = self.font.render("New",1,(10,10,10))
        self.textpos = self.rect

    def click(self):
        pos = pygame.mouse.get_pos()
        mouse_rect = pygame.rect.Rect(pos,pos)
        return self.rect.colliderect(mouse_rect)

    def bump(self):
        #self.rect.x += 10
        self.image.fill(RED)

    def unbump(self):
        #self.rect.x -= 10
        self.image.fill(GREEN)

    def display(self,screen):
        screen.blit(self.text,self.textpos)


def main():
    pygame.init()
    screen = pygame.display.set_mode((300,300))
    pygame.display.set_caption("Menu")
    #pygame.mouse.set_visible(1)

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))

    bg_image = pygame.image.load('icon.png')
    screen.blit(bg_image, (0,0))


    #screen.blit(background, (0,0))
    pygame.display.flip()

    mouse = Mouse()
    new = New()

    #print dir(pygame.sprite)
    sprites = pygame.sprite.Group(new)
    #allsprites = pygame.sprite.RenderPlain((new,mouse))

    new.display(screen)

    going = True
    while going:
        for event in pygame.event.get():
            if event.type == QUIT:
                going = False
            elif event.type == MOUSEBUTTONDOWN:
                if new.click():
                    print "hello world"
                    new.bump()
            elif event.type == MOUSEBUTTONUP:
                if new.click():
                    new.unbump()
        sprites.update()

        screen.blit(bg_image, (0,0))

        sprites.draw(screen)
        new.display(screen)
        pygame.display.flip()

    pygame.quit()

if __name__ == '__main__':
    main()

