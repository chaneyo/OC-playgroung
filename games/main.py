import pygame
import random
pygame.init()

screen = pygame.display.set_mode((800, 600))

# title
pygame.display.set_caption("Othman's Invaders")
icon = pygame.image.load('joelsm2.png')
pygame.display.set_icon(icon)

# player
playerImg = pygame.image.load('joelsm2.png')
playerX = 370
playerY = 480
playerX_change = 0

# enemy
# player
enemyImg = pygame.image.load('othmanship.png')
enemyX = random.randint(0, 800)
enemyY = random.randint(0, 150)
enemyX_change = 0.3
enemyY_change = 30


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


# game loop
running = True
while running:
    screen.fill((0, 25, 20))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            print("A keystroke is pressed")
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
                print("Left arrow is pressed")
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3
                print("Right arrrow is pressed")
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
                print("keystroke has been released")

    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    enemyX += enemyX_change
    if enemyX <= 0:
        enemyX_change = 0.3
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -0.3
        enemyY += enemyY_change

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
