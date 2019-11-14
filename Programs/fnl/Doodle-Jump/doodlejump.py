# Chase Hall & [[REDACTED]]
#
import pygame
from pygame.locals import *
import sys
import random
w = 800
h = 600
s = pygame.display.set_mode((w, h))
pygame.font.init()
f = pygame.font.SysFont("Times New Roman", 25)
class dh:
    def __init__(self):
        """
        This class loads assets and sets default values.
        """
        self.s = pygame.display.set_mode((800, 600))
        self.f = pygame.font.SysFont("Times New Roman", 25)
        self.p = pygame.image.load("assets/p.png").convert_alpha()
        self.br = pygame.image.load("assets/br.png").convert_alpha()
        self.b = pygame.image.load("assets/b.png").convert_alpha()
        self.b2 = pygame.image.load("assets/b2.png").convert_alpha()
        self.r = pygame.image.load("assets/r.png").convert_alpha()
        self.r1 = pygame.image.load("assets/r1.png").convert_alpha()
        self.l = pygame.image.load("assets/l.png").convert_alpha()
        self.l1 = pygame.image.load("assets/l1.png").convert_alpha()
        self.sp = pygame.image.load("assets/sp.png").convert_alpha()
        self.sp1 = pygame.image.load("assets/sp1.png").convert_alpha()
        self.dir = 0
        self.camy = 0
        self.j = 0
        self.score = 0
        self.gr = 0
        self.xm = 0
        self.px = 400
        self.py = 400
        self.plfms = [[400, 500, 0, 0]]
        self.spn = []
    def uP(self):
        """
        This function updates the player depending on what direction the player is facing.
        """
        if not self.j:
            self.py += self.gr
            self.gr += 1
        elif self.j:
            self.py -= self.j
            self.j -= 1
        key = pygame.key.get_pressed()
        if key[K_RIGHT]:
            if self.xm < 10:
                self.xm += 1
            self.dir = 0
        elif key[K_LEFT]:
            if self.xm > -10:
                self.xm -= 1
            self.dir = 1
        else:
            if self.xm > 0:
                self.xm -= 1
            elif self.xm < 0:
                self.xm += 1
        if self.px > 850:
            self.px = -50
        elif self.px < -50:
            self.px = 850
        self.px += self.xm
        if self.py - self.camy <= 200:
            self.camy -= 10
        if not self.dir:
            if self.j:
                self.s.blit(self.r1, (self.px, self.py - self.camy))
            else:
                self.s.blit(self.r, (self.px, self.py - self.camy))
        else:
            if self.j:
                self.s.blit(self.l1, (self.px, self.py - self.camy))
            else:
                self.s.blit(self.l, (self.px, self.py - self.camy))
    def uP2(self):
        """
        This function updates platforms and does things like collision detection.
        """
        for p in self.plfms:
            rect = pygame.Rect(p[0], p[1], self.p.get_width() - 10, self.p.get_height())
            player = pygame.Rect(self.px, self.py, self.r.get_width() - 10, self.r.get_height())
            if rect.colliderect(player) and self.gr and self.py < (p[1] - self.camy):
                if p[2] != 2:
                    self.j = 15
                    self.gr = 0
                else:
                    p[-1] = 1
            if p[2] == 1:
                if p[-1] == 1:
                    p[0] += 5
                    if p[0] > 550:
                        p[-1] = 0
                else:
                    p[0] -= 5
                    if p[0] <= 0:
                        p[-1] = 1
    def dp(self):
        """
        This function spawns (draws) the platforms
        """
        for p in self.plfms:
            check = self.plfms[1][1] - self.camy
            if check > 600:
                pl = random.randint(0, 1000)
                if pl < 800:
                    pl = 0
                elif pl < 900:
                    pl = 1
                else:
                    pl = 2
                self.plfms.append([random.randint(0, 700), self.plfms[-1][1] - 50, pl, 0])
                coords = self.plfms[-1]
                check = random.randint(0, 1000)
                if check > 900 and pl == 0:
                    self.spn.append([coords[0], coords[1] - 25, 0])
                self.plfms.pop(0)
                self.score += 100
            if p[2] == 0:
                self.s.blit(self.p, (p[0], p[1] - self.camy))
            elif p[2] == 1:
                self.s.blit(self.br, (p[0], p[1] - self.camy))
            elif p[2] == 2:
                if not p[3]:
                    self.s.blit(self.b, (p[0], p[1] - self.camy))
                else:
                    self.s.blit(self.b2, (p[0], p[1] - self.camy))
        for sp in self.spn:
            if sp[-1]:
                self.s.blit(self.sp1, (sp[0], sp[1] - self.camy))
            else:
                self.s.blit(self.sp, (sp[0], sp[1] - self.camy))
            if pygame.Rect(sp[0], sp[1], self.sp.get_width(), self.sp.get_height()).colliderect(pygame.Rect(self.px, self.py, self.r.get_width(), self.r.get_height())):
                self.j = 50
                self.camy -= 50
    def gP(self):
        """
        This function generates the platforms.
        """
        on = 600
        while on > -100:
            x = random.randint(0,700)
            pl = random.randint(0, 1000)
            if pl < 800:
                pl = 0
            elif pl < 900:
                pl = 1
            else:
                pl = 2
            self.plfms.append([x, on, pl, 0])
            on -= 50
    def run(self):
        """
        This function runs the game (spawns everything)
        """
        clock = pygame.time.Clock()
        self.gP()
        while True:
            self.s.fill((0,0,0))
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit()
            if self.py - self.camy > 700:
                self.camy = 0
                self.spn = []
                self.plfms = [[400, 500, 0, 0]]
                self.gP()
                self.px = 400
                self.py = 400
                main_menu(win)
            self.dp()
            self.uP()
            self.uP2()
            self.s.blit(self.f.render("Score: " + str(self.score), -1, (255, 255, 255)), (25, 25))
            pygame.display.flip()
def draw_text_middle(surface, text, size, color):
    """
    This function draws text on the screen for main menu + score.
    """
    f = pygame.font.SysFont("Times New Roman", size, bold=True)
    label = f.render(text, 1, color)
    surface.blit(label, (0 + w /2 - (label.get_width()/2), 0 + h/2 - label.get_height()/2))
def main_menu(win):
    """
    This function is the start menu
    """
    run = True
    j = dh()
    while run:
        win.fill((0,0,0))
        pygame.display.set_caption('Doodle Hop')
        draw_text_middle(win, 'Doodle Hop', 60, (255,255,255))
        text = f.render("Press any key to play.", 1, (255,255,255))
        s.blit(text, (300, 345))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                    j.run()
    pygame.display.quit()
win = pygame.display.set_mode((w, h))
main_menu(win)
