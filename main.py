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
        self.direction = 1
        self.flip = False
        self.animation_list = []
        self.index = 0
        for i in range(7):
            bild = pygame.image.load('Bilder/Hero Knight/Sprites/HeroKnight/Idle/{i}.png')
            bild = pygame.transform.scale(bild, (int(bild.get_width() * scale), int(bild.get_height() * scale)))
            self.animation_list.append(bild)
        self.Bilder = self.animation_list[self.index]
        self.rect = self.Bilder.get_rect()
        self.rect.center = (x,y)

    def bewegen(self, l_links, l_rechts):
        dx = 0
        dy = 0

        if l_links:
            dx = -self.speed
            self.flip = True
            self.direction = -1
        if l_rechts:
            dx = self.speed
            self.flip = False
            self.direction = 1

        self.rect.x += dx
        self.rect.y += dy


    def draw(self):
        screen.blit(pygame.transform.flip(self.Bilder, self.flip, False), self.rect)



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