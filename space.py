import random, os.path
import pygame
from pygame.locals import *
import math

SCREENRECT = Rect(0, 0, 800, 640)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
ENEMYODDS = 120
ENEMYRELOAD = 12
FPS = 70
SCORE = 0

main_dir = os.path.split(os.path.abspath(__file__))[0]

def load_image(file):
    "loads an image, prepares it for play"
    file = os.path.join(main_dir, file)
    try:
        surface = pygame.image.load(file)
    except pygame.error:
        raise SystemExit('Could not load image "%s" %s'%(file, pygame.get_error()))
    return surface.convert()


def load_images(*files):
    imgs = []
    for file in files:
        imgs.append(load_image(file))
    return imgs

def store(score):
    if not os.path.isfile('score.db'):
        conn = sqlite3.connect('score.db')
        c = conn.cursor()
        c.execute('create table SCORE(int score)')
    else:
        conn = sqlite3.connect('score.db')
        c = conn.cursor()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self,self.containers) # had self.containers
        width = 40
        height = 60
        self.image = pygame.Surface([30, 30])
        self.image = pygame.image.load("img/xwing.png");
        #self.image = pygame.transform.scale(self.image, (100, 50));
        #self.image.fill(GREEN)

        self.rect = self.image.get_rect()

        self.change_x = 1
        self.change_y = 0
        self.x = 1 * 5
        self.y = 100
        self.facing = -1
        self.rect.top = SCREENRECT.height - 100
        self.reloading = 0
        #self.rect.left = 100
        self.key = 1


    #def update(self):
        #self.rect.top += 1

    #def move(self, direction):
    #    self.rect.move_ip(direction*22, 0)




    def lift(self):
        self.rect.bottom = self.rect.bottom - 7
        #self.rect.y -= 1
        self.rect.x += 1


    def gunpos(self):
        return self.rect.midtop

    def move(self,key):
        self.key = key
        self.rect.x += ((key == K_RIGHT) - (key == K_LEFT))
        self.rect.y += (key == K_DOWN) - (key == K_UP)

    def update(self):
        self.rect.x += (self.key == K_RIGHT) - (self.key == K_LEFT)


class Enemy(pygame.sprite.Sprite):

    speed = 13
    x = 0
    images = []
    def __init__(self,game,player):
        pygame.sprite.Sprite.__init__(self, self.containers)
        #img_height = random.randint(100, 200)
        #self.image = pygame.Surface([40, 40])
        #self.image.fill(RED)
        #self.image.fill(((random.randint(0,255)), (random.randint(0, 255)), (random.randint(0, 255))))
        #self.image = pygame.image.load("enemy_1_straight.gif")
        self.image = self.images[random.randint(0, 2)]

        msk = pygame.mask.from_surface(self.image,1)

        #self.image = pygame.transform.scale(self.image, (100, 100)) # just edited this

        #print dir(self.image)
        self.rect = self.image.get_rect()
        self.x = -1
        self.y = 0
        #self.rect.top = random.choice([0, (SCREENRECT.height - img_height)])
        #if self.rect.top == 0:
        #    self.image = pygame.transform.flip(self.image, 0, 1)
        #self.rect.right = 640

        self.rect.left = random.randint(0, SCREENRECT.width)
        self.rect.top = -20
        self.game = game
        self.tick = 0
        self.tau = 0
        self.axe = 80
        self.X, self.Y = self.rect.midbottom

    #def update(self):
        #self.rect.move_ip(0, 5)
        #if self.rect.top >= SCREENRECT.height:
        #    self.game.turn = True
        #    self.kill()
        self.player = player

    def update(self):
        self.tick += 1
        self.tau += 1.8
        self.axe += 0.5
        self.X = self.axe+math.sin(math.radians(self.tau))*300
        self.Y += 0.5
        self.rect.midbottom = self.X, self.Y
        if self.rect.left < self.player.rect.centerx<self.rect.right:
            pass

class Bomb(pygame.sprite.Sprite):
    speed = 9
    image = pygame.image.load('img/oursin.png')
    def __init__(self,alien):
        pygame.sprite.Sprite.__init__(self,self.containers)
        self.rect = self.image.get_rect(midbottom=alien.rect.move(0,5).midbottom)
        self.dx = random.random()-0.5
        self.X = self.rect.x
        self.dy = 4+random.random()
        self.Y = self.rect.y

    def update(self):
        self.Y += self.dy
        self.X += self.dx
        self.x = int(self.X)
        self.y = int(self.Y)
        self.rect.x = self.x
        self.rect.y = self.y


class Gold(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        #self.image = pygame.image.load("medalGold.png")
        #self.image = pygame.transform.scale(self.image, (30, 30))
        #self.image.y = random.randint(100, 250)
        #self.image.x = 640
        #self.y = random.randint(100, 250)
        self.rect = self.image.get_rect()
        self.rect.x = 640
        #self.rect.y = 150
        self.rect.y = random.randint(100, 250)
    def update(self):
        #self.image.x = self.image.x - 1
        #self.rect.move_ip(self.x, 0)
        self.rect.x -= 1


class Score(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.Font(None, 50)
        #self.font.set_italic(1)
        self.color = Color('white')
        self.lastscore = -1
        self.update()
        self.rect = self.image.get_rect().move(10, 450)

    def update(self):
        if SCORE != self.lastscore:
            self.lastscore = SCORE
            msg = "Score: %d" % SCORE
            self.image = self.font.render(msg, 0, self.color)



class Shot(pygame.sprite.Sprite):
    speed = -11
    images = []
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self, self.containers)
        #self.image = self.images[0]
        #self.image = pygame.Surface([10, 20])
        #self.image.fill(RED)

        self.image = pygame.image.load("img/redbullet.png")

        self.rect = self.image.get_rect(midbottom=pos)

    def update(self):
        self.rect.move_ip(0, -11)
        if self.rect.right >= SCREENRECT.width:
            self.kill()



class GameOver:
    def __init__(self):
        self.turn = False


def main(winstyle = 0):
    pygame.init()
    winstyle = 0
    bestdepth = pygame.display.mode_ok(SCREENRECT.size, winstyle, 32)
    screen = pygame.display.set_mode(SCREENRECT.size, winstyle, bestdepth)
    pygame.display.set_caption('blockplane')
    pygame.mouse.set_visible(0)

    #bgtile = pygame.image.load('groundDirt.png') #chnage this to default color
    background = pygame.Surface(SCREENRECT.size)
    #background.blit(bgtile, (0, 420))

    screen.blit(background, (0, 0))
    pygame.display.flip()
    #images
    Enemy.images = load_images('img/space11.png', 'img/space12.png', 'img/space13.png')

    #initalize game objects

    enemies = pygame.sprite.Group()

    lastenemy = pygame.sprite.GroupSingle()
    #coins = pygame.sprite.Group()
    all = pygame.sprite.RenderUpdates()
    shots = pygame.sprite.Group()
    Player.containers = all
    Enemy.containers = enemies, lastenemy, all
    #Gold.containers = coins, all
    Score.containers = all
    Shot.containers = shots, all
    bombs = pygame.sprite.Group()
    Bomb.containers = bombs,all


    global SCORE
    score = 0
    enemyreload = ENEMYRELOAD

    clock = pygame.time.Clock()

    #initialize starting sprites of game

    #global SCORE
    player = Player()
    (delay, interval) = pygame.key.get_repeat()
    pygame.key.set_repeat(50,50)
    if pygame.font:
        all.add(Score())

    going = True
    game = GameOver()
    while player.alive():

        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                going = False
                return
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    player.lift()
                #if event.key == K_LEFT:
                #    player.move(-1)
                #if event.key == K_RIGHT:
                #    player.move(1)
                player.move(event.key)   # editing for better player movement

        keystate = pygame.key.get_pressed()

        all.clear(screen, background)
        all.update()

        direction = keystate[K_RIGHT] - keystate[K_LEFT]
        #player.move(direction)

        firing = keystate[K_SPACE]
        if firing and not player.reloading:
            Shot(player.gunpos())
        player.reloading = firing

        if enemyreload: #reload
            enemyreload = enemyreload - 1
        elif not int(random.random() * ENEMYODDS): #check ENEMYODDS
            Enemy(game,player)
            if random.choice([0, 1]) == 1:
                #Bomb(lastenemy.sprite)
                pass
            enemyreload = ENEMYRELOAD #check ENEMYRELOAD

        if lastenemy and not int(random.random() * 60):
            Bomb(lastenemy.sprite)
            Bomb(lastenemy.sprite)
            Bomb(lastenemy.sprite)

        for enemy in pygame.sprite.spritecollide(player, enemies, 1):
            player.kill()
        #for coin in pygame.sprite.groupcollide(shots, coins, 1, 1):
        #    coin.kill()
        #    SCORE += 1
        for enemy in pygame.sprite.groupcollide(shots, enemies, 1, 1):
            enemy.kill()
            SCORE += 1

        if SCORE == 5:
            #pygame.time.wait(1000)
            Enemy.images = []
            Enemy.images = load_images('img/square.png', 'img/square.png', 'img/square.png', 'img/square.png')

        if game.turn:
            #player.kill()
            SCORE = SCORE - 1
            game.turn = False


        dirty = all.draw(screen)
        pygame.display.update(dirty)

        clock.tick(FPS)

    pygame.time.wait(1000)
    pygame.key.set_repeat(0,0)
    pygame.quit()


if __name__ == '__main__':
    main()



