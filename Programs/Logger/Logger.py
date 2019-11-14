import pygame
from pygame.locals import *

pygame.init() # launch pygame modules (sort of like constructor)

screen = pygame.display.set_mode((150, 150))

the_log = open("Logger" , "w")

keymod = 0
while True:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            print(event.key)
            if event.key == 56:
                the_log.close()
                pygame.quit()
            elif event.key == 13:
                the_log.write("\n")
            elif event.key == 9:
                the_log.write("\t")
            elif event.key == 304 or event.key == 303:
                keymod = 32
            elif event.key < 255:
                the_log.write(chr(event.key - keymod))
        elif event.type == KEYUP:
            if event.key == 304 or event.key == 303:
                keymod = 0