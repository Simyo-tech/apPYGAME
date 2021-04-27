import pygame

pygame.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Lost Knight')

x = 200
y = 200
img = pygame.image.load('Bilder/Hero Knight/Sprites/HeroKnight/Idle/HeroKnight_Idle_0.png')
rect = img.get_rect()
rect.center = (x,y)

run = True
while run:

    screen.blit(img,rect)

    for event in pygame.event.get():
        #quit game
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()