#Imports
import pygame, sys
from pygame.locals import *
import random, time
 
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
SCORE = 0
COINS_COLLECTED = 0
COIN_THRESHOLD = 10  # Increase enemy speed once player collects this many coins
 
#Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)
 
background = pygame.image.load(r"C:\Users\User\OneDrive\Рабочий стол\ns_vs\lab_9\images\Ani.png")
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))
#Create a white screen 
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(r"C:\Users\User\OneDrive\Рабочий стол\ns_vs\lab_9\images\En.png")
        self.image = pygame.transform.scale(self.image,(40,80))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)  
 
      def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
  
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(r"C:\Users\User\OneDrive\Рабочий стол\ns_vs\lab_9\images\Play.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
        
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_UP]:
             self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
             self.rect.move_ip(0,5)
         
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"C:\Users\User\OneDrive\Рабочий стол\ns_vs\lab_9\images\Coin.png")
        self.image = pygame.transform.scale(self.image, (30, 30)) 
        self.rect = self.image.get_rect()
        # Each coin has a random value of 1, 2, or 3
        self.value = random.choice([1, 2, 3])
        # Random position on the screen
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40),random.randint(40, SCREEN_HEIGHT-200))
    def move(self):  
        pass

    def respawn(self):
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), random.randint(40, SCREEN_HEIGHT-200))
        self.value = random.choice([1, 2, 3])  # Refresh the coin's value
#Setting up Sprites        
P1 = Player()
E1 = Enemy()
coin = Coin()

#Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)

coins = pygame.sprite.Group()
coins.add(coin)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(coin) 
 
#Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)
 
#Game Loop
while True:
       
    #Cycles through all events occurring  
    for event in pygame.event.get():
        if event.type == INC_SPEED and COINS_COLLECTED >= COIN_THRESHOLD:
              SPEED += 0.5     
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.blit(background, (0,0))

    scores = font_small.render(str(SCORE), True, BLACK)
    coins_text = font_small.render("Coins: " + str(COINS_COLLECTED), True, BLACK)
    DISPLAYSURF.blit(scores, (10,10))
    DISPLAYSURF.blit(coins_text, (SCREEN_WIDTH - 100, 10))
 
    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()
    
     #To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
          pygame.mixer.Sound(r"C:\Users\User\OneDrive\Рабочий стол\ns_vs\lab_9\crash.mp3").play()
          time.sleep(0.5)
                    
          DISPLAYSURF.fill(RED)
          DISPLAYSURF.blit(game_over, (30,250))
          pygame.display.update()

          for entity in all_sprites:
                entity.kill() 
          time.sleep(2)

          pygame.quit()
          sys.exit()        

    # Collision detection between Player and Coin
    collided_coin = pygame.sprite.spritecollideany(P1, coins)
    if collided_coin:
        # Increase coins collected by the coin's value
        COINS_COLLECTED += collided_coin.value
        # Respawn the coin to a new location with a new random value
        collided_coin.respawn()

    pygame.display.update()
    FramePerSec.tick(FPS)