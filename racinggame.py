from boundary import Boundary
from checkpoint import Checkpoint
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
walls.append(Boundary(200, 180, 186, 137))
walls.append(Boundary(186, 137, 221, 120))
walls.append(Boundary(221, 120, 424, 165))
walls.append(Boundary(424, 165, 525, 92))
walls.append(Boundary(525, 92, 553, 116))
walls.append(Boundary(553, 116, 540, 186))
walls.append(Boundary(540, 186, 323, 207))
walls.append(Boundary(323, 207, 239, 375))
walls.append(Boundary(239, 375, 455, 557))
walls.append(Boundary(455, 557, 616, 445))
walls.append(Boundary(616, 445, 802, 330))
walls.append(Boundary(802, 330, 914, 172))
walls.append(Boundary(914, 172, 1061, 179))
walls.append(Boundary(1061, 179, 1100, 284))
walls.append(Boundary(1100, 284, 956, 378))
walls.append(Boundary(956, 378, 984, 508))
walls.append(Boundary(984, 508, 1152, 606))
walls.append(Boundary(1152, 606, 1152, 634))
walls.append(Boundary(1152, 634, 1061, 645))
walls.append(Boundary(1061, 645, 959, 620))
walls.append(Boundary(959, 620, 893, 526))
walls.append(Boundary(893, 526, 616, 529))
walls.append(Boundary(616, 529, 473, 602))
walls.append(Boundary(473, 602, 249, 575))
walls.append(Boundary(249, 575, 186, 466))
walls.append(Boundary(186, 466, 214, 319))
walls.append(Boundary(214, 319, 200, 200))

checkpoints = []
checkpoints.append(Checkpoint(100, 200, 200, 200, 0))
checkpoints.append(Checkpoint(100, 180, 200, 180, 1))
checkpoints.append(Checkpoint(100, 100, 186, 137, 2))
checkpoints.append(Checkpoint(200, 50, 221, 120, 3))
checkpoints.append(Checkpoint(415, 90, 424, 165, 4))
checkpoints.append(Checkpoint(531, 20, 525, 92, 5))
checkpoints.append(Checkpoint(622, 73, 553, 116, 6))
checkpoints.append(Checkpoint(591, 220, 540, 186, 7))
checkpoints.append(Checkpoint(405, 262, 323, 207, 8))
checkpoints.append(Checkpoint(322, 367, 239, 375, 9))
checkpoints.append(Checkpoint(458, 475, 455, 557, 10))
checkpoints.append(Checkpoint(563, 350, 616, 445, 11))
checkpoints.append(Checkpoint(713, 287, 802, 330, 12))
checkpoints.append(Checkpoint(867, 62, 914, 172, 13))
checkpoints.append(Checkpoint(1120, 118, 1061, 179, 14))
checkpoints.append(Checkpoint(1242, 325, 1100, 284, 15))
checkpoints.append(Checkpoint(1057, 416, 956, 378, 16))
checkpoints.append(Checkpoint(1067, 479, 984, 508, 17))
checkpoints.append(Checkpoint(1253, 559, 1152, 606, 18))
checkpoints.append(Checkpoint(1249, 643, 1152, 634, 19))
checkpoints.append(Checkpoint(1109, 700, 1061, 645, 20))
checkpoints.append(Checkpoint(882, 692, 959, 620, 21))
checkpoints.append(Checkpoint(833, 584, 893, 526, 22))
checkpoints.append(Checkpoint(657, 577, 616, 529, 23))
checkpoints.append(Checkpoint(497, 671, 473, 602, 24))
checkpoints.append(Checkpoint(164, 636, 249, 575, 25))
checkpoints.append(Checkpoint(70, 465, 186, 466, 26))
checkpoints.append(Checkpoint(126, 318, 214, 319, 27))

particle = Particle(500, 500, 10)

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

    for checkpoint in checkpoints:
        checkpoint.show(GAME_SURFACE)

    particle.cast(GAME_SURFACE, walls)

    particle.position_at(pygame.mouse.get_pos())
    # particle.show(GAME_SURFACE)

    pygame.display.update()
    CLOCK.tick(60)

pygame.quit()
quit()
