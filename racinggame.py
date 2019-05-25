from car import Car
from map import Map
import pygame
import random

# Define constants
DISPLAY_WIDTH = 1280
DISPLAY_HEIGHT = 720
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

pygame.init()
pygame.display.set_caption(f"Racinggame")

CLOCK = pygame.time.Clock()

GAME_SURFACE = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

BACKGROUND = pygame.Surface(GAME_SURFACE.get_size())
BACKGROUND = BACKGROUND.convert()
BACKGROUND.fill(BLACK)

GAME_QUIT = False

mymap = Map()
c = Car(150, 190, 270)

keys = [False, False, False, False]  # up, down, left, right

while not GAME_QUIT:

    GAME_SURFACE.blit(BACKGROUND, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GAME_QUIT = True
        elif event.type == pygame.KEYDOWN:
            if event.key == 273:  # up
                keys[0] = True
            elif event.key == 274:  # down
                keys[1] = True
            elif event.key == 276:  # left
                keys[2] = True
            elif event.key == 275:  # right
                keys[3] = True
        elif event.type == pygame.KEYUP:
            if event.key == 273:  # up
                keys[0] = False
            elif event.key == 274:  # down
                keys[1] = False
            elif event.key == 276:  # left
                keys[2] = False
            elif event.key == 275:  # right
                keys[3] = False
        # else:
        #    print(event)
        #    pass

    mymap.show_walls(GAME_SURFACE)
    # mymap.show_checkpoints(GAME_SURFACE)

    c.update(keys)
    c.show(GAME_SURFACE)
    c.cast(GAME_SURFACE, mymap.walls)

    pygame.display.update()
    CLOCK.tick(60)

pygame.quit()
quit()
