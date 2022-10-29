import random
import pygame
pygame.init()
#screen
screen = pygame.display.set_mode((800,600))

#background 
bakcground = pygame.image.load('Images/background.png')


#Title and Icon
pygame.display.set_caption("Space invaders")
icon = pygame.image.load('Images/ufo.png')
pygame.display.set_icon(icon)

#player 
playerimg = pygame.image.load('Images/launch.png')
playerX = 370
playerY = 480
playerX_changes = 0

#alien 
alienimg = pygame.image.load('Images/alien.png')
alienX = random.randint(0,800)
alienY = random.randint(50,150)
alienX_changes = 0.3
alienY_changes = 40

#bullet
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
    #screen color

    screen.fill((200,0,00))
    #background
    screen.blit(bakcground,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #keystroke is pressed
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            playerX_changes = -0.8
        if event.key == pygame.K_RIGHT:
            playerX_changes = 0.8
        if event.key == pygame.K_SPACE:
            fire_bullet(playerX,bulletY)
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            playerX_changes = 0

    playerX += playerX_changes

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    alienX += alienX_changes

    if alienX <= 0:
        alienX_changes = 0.4
        alienY += alienY_changes
    elif alienX >= 736 :
        alienX_changes = -0.4
        alienY += alienY_changes

    # bullet movement
    if bullet_state is "fired":
        fire_bullet(playerX,bulletY)
        bulletY -= bulletY_changes 

    #displaying player
    player(playerX,playerY)
    alien(alienX,alienY)
    pygame.display.update()