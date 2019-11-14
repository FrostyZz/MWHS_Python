import pygame
from pygame.locals import *

def timerFunc():
    print("Timer CallBack")

pygame.init()
pygame.time.set_timer(USEREVENT+1, 100)
while 1:
    for event in pygame.event.get():
        if event.type == USEREVENT+1:
            timerFunc()
        if event.type == QUIT:
            break