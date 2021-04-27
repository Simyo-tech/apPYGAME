import pygame

pygame.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Lost Knight')

#Bildwiederholungsrate
clock = pygame.time.Clock()
FPS = 120

#Spieler Aktion-variablen
l_links = False
l_rechts = False

#Farben Definitionen
BG = (240, 255, 255)

def draw_bg():
    screen.fill(BG)


class Figur(pygame.sprite.Sprite):
    def __init__(self, x, y, scale, speed):
        pygame.sprite.Sprite.__init__(self)
        self.speed = speed
        bild = pygame.image.load('Bilder/Hero Knight/Sprites/HeroKnight/Idle/HeroKnight_Idle_0.png')
        self.Bilder = pygame.transform.scale(bild, (int(bild.get_width() * scale), int(bild.get_height() * scale)))
        self.rect = self.Bilder.get_rect()
        self.rect.center = (x,y)

    def bewegen(self, l_links, l_rechts):
        dx = 0
        dy = 0

        if l_links:
            dx = -self.speed
        if l_rechts:
            dx = self.speed

        self.rect.x += dx
        self.rect.y += dy


    def draw(self):
        screen.blit(self.Bilder, self.rect)



spieler  = Figur(200, 500, 2, 9)

run = True
while run:

    clock.tick(FPS)
    draw_bg()

    spieler.draw()
    spieler.bewegen(l_links, l_rechts)


    for event in pygame.event.get():
        #quit game
        if event.type == pygame.QUIT:
            run = False
        #keyboard presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                l_links = True
            if event.key == pygame.K_d:
                l_rechts = True
            if event.key == pygame.K_ESCAPE:
                run = False

        #keyboard button released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                l_links = False
            if event.key == pygame.K_d:
                l_rechts = False


    pygame.display.update()

pygame.quit()