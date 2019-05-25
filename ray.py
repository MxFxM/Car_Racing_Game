import math
import pygame

WHITE = (255, 255, 255)


class Ray:

    def __init__(self, x1, y1, a):
        self.position = (x1, y1)
        x_part = math.cos(2 * math.pi * a / 360)
        y_part = math.sin(2 * math.pi * a / 360)
        self.direction = (x_part, y_part)

    def show(self, surface):
        endpos = [round(p+d*10)
                  for p, d in zip(self.position, self.direction)]
        pygame.draw.line(surface, WHITE, self.position, endpos)

    def look_at_angle(self, angle):
        x_part = math.cos(2 * math.pi * angle / 360)
        y_part = math.sin(2 * math.pi * angle / 360)
        self.direction = (x_part, y_part)

    def position_at(self, pos):
        self.position = pos

    def cast(self, boundary):
        # math from wikipedia but a bit changed because ray is not the full line
        x1 = boundary.a_pos[0]
        y1 = boundary.a_pos[1]
        x2 = boundary.b_pos[0]
        y2 = boundary.b_pos[1]

        x3 = self.position[0]
        y3 = self.position[1]
        x4 = self.position[0] + self.direction[0]
        y4 = self.position[1] + self.direction[1]

        denominator = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)

        if denominator == 0:
            return False

        t = (x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)
        t = t / denominator

        u = (x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)
        u = -u / denominator

        if t > 0 and t < 1 and u > 0:
            # intersection on boundary segment and in positive rayy direction
            return (round(x1 + t * (x2 - x1)), round(y1 + t * (y2 - y1)))
        return False


if __name__ == '__main__':
    print("Please run raycasting.py as main.")
