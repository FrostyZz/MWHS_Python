import pygame
DULLGREEN = (55, 154, 54)
DULLYELLOW = (156, 157, 50)
DULLRED = (153, 50, 51)
RED = (255, 0, 0)
YELLOW = (252, 255, 31)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
pygame.init()
size = (175, 175)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Traffic Light")
clock = pygame.time.Clock()
FPS = 15
done = False
light_on = 0
LIGHTS_EVENT = pygame.USEREVENT + 0
pygame.time.set_timer(LIGHTS_EVENT, 3000)
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == LIGHTS_EVENT:
            light_on += 1
            if light_on == 3:
                light_on = 0
    currentTopColor = DULLRED
    currentMiddleColor = DULLYELLOW
    currentBottomColor = DULLGREEN
    if light_on == 0:
        currentTopColor = RED
    if light_on == 1:
        currentBottomColor = GREEN
    if light_on == 2:
        currentMiddleColor = YELLOW
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLACK, [50, 5, 50, 100], 0)
    pygame.draw.rect(screen,BLACK, [65, 100, 20, 40], 0)
    pygame.draw.circle(screen, currentTopColor, [75, 20], 12)
    pygame.draw.circle(screen, currentMiddleColor, [75, 50], 12)
    pygame.draw.circle(screen, currentBottomColor, [75, 80], 12)
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()