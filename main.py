import pygame
import os
import sys

pygame.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Lost Knight')
hintergrund = pygame.image.load("Bilder/Hintergrund/parallax_mountain_pack/layers/parallax-mountain-bg.png").convert()

#Bildwiederholungsrate
clock = pygame.time.Clock()
FPS = 120

#Gravitation
GRAVITATION = 0.75

#Spieler Aktion-variablen
main = False
l_links = False
l_rechts = False
g_links = False
g_rechts = False

#Farben Definitionen
BG = (240, 255, 255)
RED = (255, 0, 0)
def draw_bg():
    screen.fill(BG)
    size = (1280, 720)
    #pygame.draw.line(screen, RED, (0, 500), (SCREEN_WIDTH, 500))
    screen.blit(pygame.transform.scale(hintergrund,size),(0,0))




class Figur(pygame.sprite.Sprite):
    def __init__(self, figur_typ, x, y, scale, speed):
        pygame.sprite.Sprite.__init__(self)
        self.figur_typ = figur_typ
        self.lebendig = True
        self.speed = speed
        self.leben = 100
        self.max_leben = self.leben
        self.s_hoehe_y = 0
        self.richtung = 1
        self.sprung = False
        self.in_luft = True
        self.drehen = False
        self.animation_list = []
        self.bild_index = 0
        self.aktion = 0
        self.angriff = False
        self.update_time = pygame.time.get_ticks()


        animationstypen = ['Idle', 'Run', 'Jump', 'Attack1', 'Death']
        for animation in animationstypen:
            #Bilder zurücksetzen
            temp_list = []
            #Anzahl Bilder zählen
            anzahl_bilder = len(os.listdir(f'Bilder/HeroKnight/Sprites/{self.figur_typ}/{animation}'))
            for i in range(anzahl_bilder-1):
                bild = pygame.image.load(f'Bilder/HeroKnight/Sprites/{self.figur_typ}/{animation}/{self.figur_typ}_{animation}_{i}.png')
                bild = pygame.transform.scale(bild, (int(bild.get_width() * scale), int(bild.get_height() * scale)))
                temp_list.append(bild)
            self.animation_list.append(temp_list)

        self.Bilder = self.animation_list[self.aktion][self.bild_index]
        self.rect = self.Bilder.get_rect()
        self.rect.center = (x,y)

    def spieler_bewegen(self, l_links, l_rechts):
        dx = 0
        dy = 0

        if spieler.sprung == True and spieler.in_luft == False:
            spieler.s_hoehe_y = -15
            spieler.sprung = False
            spieler.in_luft = True

        #Gravitation einfügen
        spieler.s_hoehe_y += GRAVITATION
        if spieler.s_hoehe_y > 15:
            spieler.s_hoehe_y
        dy += spieler.s_hoehe_y

        #Kollision checken mit Boden checken
        if spieler.rect.bottom + dy > 500:
            dy = 500 - spieler.rect.bottom
            spieler.in_luft = False

        if spieler.angriff == True and spieler.bild_index == 5:
            spieler.angriff = False

        if l_links:
            dx = -spieler.speed
            spieler.drehen = True
            spieler.richtung = -1
        if l_rechts:
            dx = spieler.speed
            spieler.drehen = False
            spieler.richtung = 1

        spieler.rect.x += dx
        spieler.rect.y += dy


    def gegner_bewegen(self, g_links, g_rechts):
        dx = 0
        dy = 0

        if gegner2.sprung == True and gegner2.in_luft == False:
            gegner2.s_hoehe_y = -15
            gegner2.sprung = False
            gegner2.in_luft = True

        #Gravitation einfügen
        gegner2.s_hoehe_y += GRAVITATION
        if gegner2.s_hoehe_y > 15:
            gegner2.s_hoehe_y
        dy += gegner2.s_hoehe_y

        #Kollision checken mit Boden checken
        if gegner2.rect.bottom + dy > 500:
            dy = 500 - gegner2.rect.bottom
            gegner2.in_luft = False

        if gegner2.angriff == True and gegner2.bild_index == 5:
            gegner2.angriff = False

        if g_links:
            dx = -gegner2.speed
            gegner2.drehen = True
            gegner2.richtung = -1
        if g_rechts:
            dx = gegner2.speed
            gegner2.drehen = False
            gegner2.richtung = 1

        gegner2.rect.x += dx
        gegner2.rect.y += dy



    def update_animation(self):
        # Bildreihenfolge
        ANIMATION_COOLDOWN = 100
        self.Bilder = self.animation_list[self.aktion][self.bild_index]
        #überprüfe ob genügend Zeit vergangen ist seit letztem Update
        if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
            self.update_time = pygame.time.get_ticks()
            self.bild_index += 1
        #wenn alle Bilder durchgelaufen sind wieder von vorne
        if self.bild_index >= len(self.animation_list[self.aktion]):
            self.bild_index = 0

    def update_aktion(self, neue_aktion):
        if neue_aktion != self.aktion:
            self.aktion = neue_aktion
            self.bild_index = 0
            self.update_time = pygame.time.get_ticks()


    def draw(self):
        screen.blit(pygame.transform.flip(self.Bilder, self.drehen, False), self.rect)

    def tod(self):
        if self.leben == 0:
            self.lebendig = False
            if self.lebendig == False and self.bild_index == 4:
                self.rect.y = -300


spieler = Figur('HeroKnight', 200, 500, 2, 5)

gegner2 = Figur('Gegner', 600, 500, 0.2, 5)


run = True
while run:

    clock.tick(FPS)
    draw_bg()

    spieler.update_animation()

    gegner2.update_animation()
    spieler.draw()

    gegner2.draw()

    spieler.tod()
    gegner2.tod()


    #Spieler Aktion Auswahl
    if spieler.lebendig:
        if spieler.in_luft:
            spieler.update_aktion(2)#2: springen
            #gegner1.update_aktion(0)
        elif l_links or l_rechts:
            spieler.update_aktion(1)#1: rennen
            #gegner1.update_aktion(1)
        elif spieler.angriff:
            spieler.update_aktion(3)
            #gegner1.update_aktion(3)
        else:
            spieler.update_aktion(0)#0: stehen
        spieler.spieler_bewegen(l_links, l_rechts)

    if gegner2.lebendig:
        if gegner2.in_luft:
            gegner2.update_aktion(2)  # 2: springen
        elif g_links or g_rechts:
            gegner2.update_aktion(1)  # 1: rennen
            # gegner1.update_aktion(1)
        elif gegner2.angriff:
            gegner2.update_aktion(3)
        else:
            gegner2.update_aktion(0)
        gegner2.gegner_bewegen(g_links, g_rechts)

    if gegner2.lebendig == False:
            gegner2.update_aktion(4)
            if gegner2.bild_index == 4:
                hintergrund = pygame.image.load(
                    "Bilder/Hintergrund/parallax_mountain_pack/layers/hi.jpg").convert()

    if spieler.lebendig == False:
            spieler.update_aktion(4)
            if spieler.bild_index == 4:
                hintergrund = pygame.image.load(
                    "Bilder/Hintergrund/parallax_mountain_pack/layers/hi.jpg").convert()



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
            if event.key == pygame.K_LEFT:
                g_links = True
            if event.key == pygame.K_RIGHT:
                g_rechts = True
            if event.key == pygame.K_w and spieler.lebendig:
                spieler.sprung = True
            if event.key == pygame.K_UP and gegner2.lebendig:
                gegner2.sprung = True
            if event.key == pygame.K_SPACE:
                spieler.angriff = True
                if pygame.sprite.collide_rect(spieler, gegner2):
                    if gegner2.lebendig:
                        gegner2.leben -= 25
                        print(gegner2.leben)
            if event.key == pygame.K_RSHIFT:
                gegner2.angriff = True
                if pygame.sprite.collide_rect(gegner2, spieler):
                    if spieler.lebendig:
                        spieler.leben -= 25
                        print(spieler.leben)
            if event.key == pygame.K_ESCAPE:
                run = False
            if event.key == pygame.K_RETURN and spieler.lebendig == False:
                os.execl(sys.executable, sys.executable, *sys.argv)
            if event.key == pygame.K_RETURN and gegner2.lebendig == False:
                os.execl(sys.executable, sys.executable, *sys.argv)

        #keyboard button released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                l_links = False
            if event.key == pygame.K_d:
                l_rechts = False
            if event.key == pygame.K_LEFT:
                g_links = False
            if event.key == pygame.K_RIGHT:
                g_rechts = False




    pygame.display.update()

pygame.quit()