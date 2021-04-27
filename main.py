import pygame

pygame.init()

SCREEN_WIDTH = 854
SCREEN_HEIGHT = 480

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Lost Knight')

run = True
while run:
    for event in pygame.event.get():
        #quit game
        if event.type == pygame.QUIT:
            run = False

pygame.quit()