from boundary import Boundary
from particle import Particle
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

walls = []
# Outer boundaries
walls.append(Boundary(100, 200, 100, 180))
walls.append(Boundary(100, 180, 100, 100))
walls.append(Boundary(100, 100, 200, 50))
walls.append(Boundary(200, 50, 415, 90))
walls.append(Boundary(415, 90, 531, 20))
walls.append(Boundary(531, 20, 622, 73))
walls.append(Boundary(622, 73, 591, 220))
walls.append(Boundary(591, 220, 405, 262))
walls.append(Boundary(405, 262, 322, 367))
walls.append(Boundary(322, 367, 458, 475))
walls.append(Boundary(458, 475, 563, 350))
walls.append(Boundary(563, 350, 713, 287))
walls.append(Boundary(713, 287, 867, 62))
walls.append(Boundary(867, 62, 1120, 118))
walls.append(Boundary(1120, 118, 1242, 325))
walls.append(Boundary(1242, 325, 1057, 416))
walls.append(Boundary(1057, 416, 1067, 479))
walls.append(Boundary(1067, 479, 1253, 559))
walls.append(Boundary(1253, 559, 1249, 643))
walls.append(Boundary(1249, 643, 1109, 700))
walls.append(Boundary(1109, 700, 882, 692))
walls.append(Boundary(882, 692, 833, 584))
walls.append(Boundary(833, 584, 657, 577))
walls.append(Boundary(657, 577, 497, 671))
walls.append(Boundary(497, 671, 164, 636))
walls.append(Boundary(164, 636, 70, 465))
walls.append(Boundary(70, 465, 126, 318))
walls.append(Boundary(126, 318, 100, 200))

# Inner boundaries
walls.append(Boundary(200, 200, 200, 180))


particle = Particle(500, 500, 360)

px = 0
py = 0

while not GAME_QUIT:

    GAME_SURFACE.blit(BACKGROUND, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GAME_QUIT = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            m = pygame.mouse.get_pos()
            mx = m[0]
            my = m[1]
            print(f"walls.append(Boundary({px}, {py}, {mx}, {my}))")
            px = mx
            py = my
        else:
            # print(event)
            pass

    for wall in walls:
        wall.show(GAME_SURFACE)

    particle.cast(GAME_SURFACE, walls)

    particle.position_at(pygame.mouse.get_pos())
    # particle.show(GAME_SURFACE)

    pygame.display.update()
    CLOCK.tick(60)

pygame.quit()
quit()
