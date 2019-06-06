from population import Population
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
test_population = Population(100, 10, 10)
# c = Car(150, 190, 270)

keys = [False, False, False, False]  # up, down, left, right

while not GAME_QUIT:

    GAME_SURFACE.blit(BACKGROUND, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GAME_QUIT = True
        # else:
        #    print(event)
        #    pass

    mymap.show_walls(GAME_SURFACE)
    mymap.show_checkpoints(GAME_SURFACE)

    test_population.update(GAME_SURFACE, mymap.walls, mymap.checkpoints)
    test_population.show(GAME_SURFACE)

    if test_population.done():
        test_population.calculatefitness()
        test_population.selection()
        test_population.mutation()
    # cast was moved to popultaion update

    pygame.display.update()
    CLOCK.tick(60)

pygame.quit()
quit()
