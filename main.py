# random is used for enemy for there locations 
# pygame is used for doing game stuff like screen ,background , player movement ,etc.

import random
import pygame

pygame.init()

#Display Screen 
screen = pygame.display.set_mode((800,600))

#Background Image of Game
bakcground = pygame.image.load('Images/background.png')

#Game Title and Logo 
pygame.display.set_caption("Space invaders")
icon = pygame.image.load('Images/ufo.png')
pygame.display.set_icon(icon)

#player (Space-ship)
playerimg = pygame.image.load('Images/launch.png')
playerX = 370
playerY = 480
playerX_changes = 0

#enemy (Alien)
alienimg = pygame.image.load('Images/alien.png')
alienX = random.randint(0,800)
alienY = random.randint(50,150)
alienX_changes = 0.3
alienY_changes = 40

#bullet (space craft missile)
bulletimg = pygame.image.load('Images/bullet.png')
bulletX =0
bulletY = 480 
bulletX_changes = 0.3
bulletY_changes = 0.1
bullet_state = "ready"


def player(x,y):
    screen.blit(playerimg,(x,y))

def alien(x,y):
    screen.blit(alienimg,(x,y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fired"
    screen.blit(bulletimg,(x + 16,y + 10))

#Game loop 
running = True
while running:

    #screen color if you don't use background images
    # screen.fill((200,0,00))

    # Setting(Calling) Background image
    screen.blit(bakcground,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #keystroke is pressed (Game Controller's '<-','->','space_bar')
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            playerX_changes = -0.8
        if event.key == pygame.K_RIGHT:
            playerX_changes = 0.8
        if event.key == pygame.K_SPACE:
            if bullet_state is "ready" :
                bulletX == playerX
                fire_bullet(playerX,bulletY)
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            playerX_changes = 0

#increse the positions for transition of movements By Based on Controllers
    playerX += playerX_changes

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

#increase the positions for transition of movements By Defaults 
    alienX += alienX_changes


    if alienX <= 0:
        alienX_changes = 0.4
        alienY += alienY_changes
    elif alienX >= 736 :
        alienX_changes = -0.4
        alienY += alienY_changes

    # bullet movement (When user press the space_bar)
    if bullet_state is "fired":
        fire_bullet(playerX,bulletY)
        bulletY -= bulletY_changes 

    #displaying player
    player(playerX,playerY)
    alien(alienX,alienY)
    pygame.display.update()