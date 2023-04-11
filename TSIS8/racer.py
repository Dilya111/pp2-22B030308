import pygame
import random
import time
from math import *

pygame.init()
clock = pygame.time.Clock()
w = 400
h = 600
SPEED = 3
coin_speed = 3
SCORE = 0
SCORE2 = 0

sc = pygame.display.set_mode((w,h))
pygame.display.set_caption("Game")
WHITE = (255, 255, 255)
RED = (255,0,0)
BLACK = (0,0,0)
sc.fill(WHITE)

font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

bg = pygame.image.load('racer\\AnimatedStreet.png')

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('racer\\Enemy.png')
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, w-40),0)
        # self.image = pygame.image.load("Enemy.png")
        # self.rect = self.image.get_rect(center =(random.randint(40,w-40),0))

    def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if(self.rect.top > h):
            self.rect.top = 0
            self.rect.center = (random.randint(40,w-40),0)
    
    def draw(self,surface):
        surface.blit(self.image, self.rect)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('racer\\Player.png')
        self.rect = self.image.get_rect()
        self.rect.center = (160,520)
    
    def move(self):
        if event.type == pygame.KEYDOWN:
            # if event.key == pygame.K_UP:
            #     self.rect.move_ip(0,-5)
            # if event.key == pygame.K_DOWN:
            #     self.rect.move_ip(0,5)
            if event.key == pygame.K_LEFT and self.rect.left>0:
                self.rect.move_ip(-5,0)
            if event.key == pygame.K_RIGHT and self.rect.right<w:
                self.rect.move_ip(5,0)


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('racer\\coin.png')
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,w-40),0)
    
    def move(self):
        self.rect.move_ip(0,coin_speed)
        self.image = pygame.transform.scale(self.image,(30,30))
        if(self.rect.top > 422):
            self.rect.center = (random.randint(40,w-40),0)
      
    def draw(self,surface):
        surface.blit(self.image, self.rect)

class Coin_2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('racer\\coin2.png')
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,w-40),0)

    def move(self):
        self.rect.move_ip(0,coin_speed)
        self.image = pygame.transform.scale(self.image,(30,30))
        if(self.rect.top>426):
            self.rect.center = (random.randint(40,w-40), 0)

    def draw(self,surface):
        surface.blit(self.image, self.rect)
E1 = Enemy()
C1 = Coin()
C2 = Coin_2()
P1 = Player()
enemies = pygame.sprite.Group()
enemies.add(E1)

all_sprites = pygame.sprite.Group()
all_sprites.add(E1)
all_sprites.add(C1)
all_sprites.add(P1)
single_sprite = pygame.sprite.Group()
single_sprite.add(C2)

coins = pygame.sprite.Group()
coins.add(C1)

coins_2 = pygame.sprite.Group()
coins_2.add(C2)

INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

run = True
while run:
    for event in pygame.event.get():
        # if event.type == INC_SPEED:
        #     SPEED+=0.5
        if event.type == pygame.QUIT:
            run = False
    
    sc.blit(bg,(0,0))
    scores = font_small.render(str(SCORE), True, BLACK)
    sc.blit(scores, (20,10))

    for entity in all_sprites:
        sc.blit(entity.image, entity.rect)
        entity.move()
    
    if pygame.sprite.spritecollideany(P1, coins):
        SCORE2 = SCORE+1
        SCORE+=1
        

    if pygame.sprite.spritecollideany(P1, coins_2):
        SCORE = SCORE+3

    if SCORE%5==0 and SCORE>0:
        SPEED += 0.009
        
    n = random.randint(1,10)
    if SCORE%n==0 and SCORE>0:
        for entity in single_sprite:
            sc.blit(entity.image, entity.rect)
            entity.move()
        
    
        


    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('racer\\crash.wav').play()
        time.sleep(0.5)

        sc.fill(RED)
        sc.blit(game_over, (30,250))
        pygame.display.update()
        
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()

    pygame.display.update()
    clock.tick(60)