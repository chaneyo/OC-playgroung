import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

#title
pygame.display.set_caption("Othman's Invaders")
icon = pygame.image.load('joelsm2.png')
pygame.display.set_icon(icon)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 25, 20))
    pygame.display.update()
