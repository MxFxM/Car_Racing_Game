import pygame


GREEN = (0, 255, 0)


class Checkpoint:

    def __init__(self, x1, y1, x2, y2):
        self.a_pos = (x1, y1)
        self.b_pos = (x2, y2)

    def show(self, surface):
        pygame.draw.line(surface, GREEN, self.a_pos, self.b_pos)


if __name__ == '__main__':
    print("Please run racinggame.py as main.")
