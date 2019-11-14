import pygame

pygame.init()

screen_width = 800
screen_height = 600
FPS = 60

screen = pygame.display.set_mode((screen_width, screen_height))
white = (255,255,255)
screen.fill(white)
bee_Img = pygame.image.load("Bee.png")

clock = pygame.time.Clock() # gives us refresh rate

def bee(x,y):
    screen.blit(bee_Img, (x,y))
    
def game():
    exit_game = False
    curr_x = (screen_width * .45)
    curr_y = (screen_height * .45)
    x_key_mod = 0
    y_key_mod = 0
    while not exit_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_key_mod -= 5
                elif event.key == pygame.K_RIGHT:
                    x_key_mod += 5
                elif event.key == pygame.K_DOWN:
                    y_key_mod += 5
                elif event.key == pygame.K_UP:
                    y_key_mod -= 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    x_key_mod +=  5
                elif event.key == pygame.K_RIGHT:
                    x_key_mod -= 5
                elif event.key == pygame.K_DOWN:
                    y_key_mod -= 5
                elif event.key == pygame.K_UP:
                    y_key_mod += 5
        curr_x += x_key_mod
        curr_y += y_key_mod
        if curr_x > screen_width -100 or curr_x < 0:
            exit_game = True
        elif curr_y > screen_height -100 or curr_y < 0:
            exit_game = True
        screen.fill(white)
        bee(curr_x, curr_y)
        pygame.display.update()
        clock.tick(FPS)
    
game()