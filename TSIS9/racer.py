
import pygame, sys
from pygame.locals import *
from random import randint
import time

#Initialzing 
pygame.init()

#Setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()


#Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SPEED_ENEMY = 5
SCORE = 0
SCORE_COIN = 0
bg_y = 0

#Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

background = pygame.image.load("pic/AnimatedStreet.png")

#Create a white screen 
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")


class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("pic/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (randint(50,SCREEN_WIDTH-50), 0)

      def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED_ENEMY)
        if (self.rect.bottom > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (randint(50, SCREEN_WIDTH - 50), 0)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("pic/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
       
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)
class Coin(pygame.sprite.Sprite):
    #Генерация монеток
    def __init__(self, image, weight):
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.center = (randint(40, 360), randint(-100, 0))
        self.weight = weight
        self.mask = pygame.mask.from_surface(self.image)

    #Движение монеток схожи с движением вражеской машины. Количество монеток можно изменить ниже
    def move(self):
        global SCORE_COIN
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.top = 0
            self.rect.center = (randint(40, 360), 0)
        elif pygame.sprite.spritecollide(self, player , False, pygame.sprite.collide_mask):
            SCORE_COIN += self.weight
            self.rect.top = 0
            self.rect.center = (randint(40,360), 0)
        elif pygame.sprite.spritecollideany(self, enemies, pygame.sprite.collide_mask):
            self.rect.center = (randint(40,450), 0)

        self.rect.move_ip(0, SPEED)

#Setting up Sprites        
P1 = Player()
E1 = Enemy()

#Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)

player = pygame.sprite.Group()
player.add(P1)

coins_group = pygame.sprite.Group()

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)

#Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

#Numbers coins
for i in range(2):
    c1 = Coin('pic/coin2.png', 1)
    coins_group.add(c1)
    all_sprites.add(c1)
for i in range(1):
    c2 = Coin('pic/coin.png', 2)
    coins_group.add(c2)
    all_sprites.add(c2)

#Game Loop
while True:
      
    #Cycles through all events occuring  
    for event in pygame.event.get():
        if event.type == INC_SPEED:
              SPEED_ENEMY += 0.05    
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.blit(background, (0,bg_y))
    DISPLAYSURF.blit(background, (0,bg_y - 600))

    bg_y += 2
    if bg_y == 600:
        bg_y = 0

    scores = font_small.render(str(SCORE), True, BLACK)
    coins_view = font_small.render(str(SCORE_COIN),True, BLACK)
    DISPLAYSURF.blit(scores, (10,10))
    DISPLAYSURF.blit(coins_view,(370,10))

    if SCORE_COIN == 20:
        SPEED_ENEMY += 0.2
    if SCORE_COIN == 40:
        SPEED_ENEMY += 0.2
    if SCORE_COIN == 60:
        SPEED_ENEMY += 0.2
        
    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)

    #To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
          pygame.mixer.Sound('pic/crash.wav').play()
          time.sleep(1)
                   
          DISPLAYSURF.fill(RED)
          DISPLAYSURF.blit(game_over, (30,250))
          
          pygame.display.update()
          for entity in all_sprites:
                entity.kill() 
          time.sleep(2)
          pygame.quit()
          sys.exit()        
        
    pygame.display.update()
    FramePerSec.tick(FPS)
