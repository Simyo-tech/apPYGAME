import pygame

pygame.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Lost Knight')


class Figur(pygame.sprite.Sprite):
    def __init__(self, x, y, scale):
        pygame.sprite.Sprite.__init__(self)
        bild = pygame.image.load('Bilder/Hero Knight/Sprites/HeroKnight/Idle/HeroKnight_Idle_0.png')
        self.Bilder = pygame.transform.scale(bild, (int(bild.get_width() * scale), int(bild.get_height() * scale)))
        self.rect = self.Bilder.get_rect()
        self.rect.center = (x,y)
    def draw(self):
        screen.blit(self.Bilder, self.rect)



spieler  = Figur(200, 200, 2)
spieler2 = Figur(400, 200, 2)

run = True
while run:

    spieler.draw()
    spieler2.draw()


    for event in pygame.event.get():
        #quit game
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()