import pygame

pygame.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Lost Knight')

#Bildwiederholungsrate
clock = pygame.time.Clock()
FPS = 120

#Gravitation
GRAVITATION = 0.75

#Spieler Aktion-variablen
l_links = False
l_rechts = False

#Farben Definitionen
BG = (240, 255, 255)
RED = (255, 0, 0)
def draw_bg():
    screen.fill(BG)
    pygame.draw.line(screen, RED, (0, 300), (SCREEN_WIDTH, 300))


class Figur(pygame.sprite.Sprite):
    def __init__(self, x, y, scale, speed):
        pygame.sprite.Sprite.__init__(self)
        self.lebendig = True
        self.speed = speed
        self.hoehe_y = 0
        self.richtung = 1
        self.sprung = False
        self.drehen = False
        self.animation_list = []
        self.bild_index = 0
        self.aktion = 0
        temp_list = []
        self.update_time = pygame.time.get_ticks()
        for i in range(8):
            bild = pygame.image.load(f'Bilder/Hero Knight/Sprites/HeroKnight/Idle/HeroKnight_Idle_{i}.png')
            bild = pygame.transform.scale(bild, (int(bild.get_width() * scale), int(bild.get_height() * scale)))
            temp_list.append(bild)
        self.animation_list.append(temp_list)
        temp_list = []
        for i in range(10):
            bild = pygame.image.load(f'Bilder/Hero Knight/Sprites/HeroKnight/Run/HeroKnight_Run_{i}.png')
            bild = pygame.transform.scale(bild, (int(bild.get_width() * scale), int(bild.get_height() * scale)))
            temp_list.append(bild)

        self.animation_list.append(temp_list)
        self.Bilder = self.animation_list[self.aktion][self.bild_index]
        self.rect = self.Bilder.get_rect()
        self.rect.center = (x,y)

    def bewegen(self, l_links, l_rechts):
        dx = 0
        dy = 0

        if self.sprung == True:
            self.hoehe_y = -11
            self.sprung = False

        self.hoehe_y += GRAVITATION
        if self.hoehe_y > 10:
            self.hoehe_y
        dy += self.hoehe_y

        #Kollision checken
        if self.rect.bottom + dy > 300:
            dy = 300 - self.rect.bottom


        if l_links:
            dx = -self.speed
            self.drehen = True
            self.richtung = -1
        if l_rechts:
            dx = self.speed
            self.drehen = False
            self.richtung = 1

        self.rect.x += dx
        self.rect.y += dy

    def update_animation(self):
        # Bildreihenfolge
        ANIMATION_COOLDOWN = 100
        self.Bilder = self.animation_list[self.aktion][self.bild_index]
        #überprüfe ob genügend Zeit vergangen ist
        if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
            self.update_time = pygame.time.get_ticks()
            self.bild_index += 1
        if self.bild_index >= len(self.animation_list[self.aktion]):
            self.bild_index = 0

    def update_aktion(self, new_action):
        if new_action != self.aktion:
            self.aktion = new_action
            self.bild_index = 0
            self.update_time = pygame.time.get_ticks()


    def draw(self):
        screen.blit(pygame.transform.flip(self.Bilder, self.drehen, False), self.rect)



spieler = Figur(200, 500, 2, 4)

run = True
while run:

    clock.tick(FPS)
    draw_bg()

    spieler.update_animation()
    spieler.draw()

    if spieler.lebendig:
        if l_links or l_rechts:
            spieler.update_aktion(1)#1: rennen
        else:
            spieler.update_aktion(0)
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
            if event.key == pygame.K_SPACE:
                spieler.sprung = True
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