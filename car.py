import pygame
import math


BLUE = (0, 0, 255)


class Car:
    def __init__(self, x1, y1, a):
        self.position = (x1, y1)
        x_part = math.cos(2 * math.pi * a / 360)
        y_part = math.sin(2 * math.pi * a / 360)
        self.direction = (x_part, y_part)
        self.angle = a
        self.vel = 2
        self.angle_vel = 5

    def show(self, surface):
        pos = (round(self.position[0]), round(self.position[1]))
        pygame.draw.circle(surface, BLUE, pos, 5)

    def update(self, keys):
        if keys[2]:
            self.angle = self.angle - self.angle_vel
            x_part = math.cos(2 * math.pi * self.angle / 360)
            y_part = math.sin(2 * math.pi * self.angle / 360)
            self.direction = (x_part, y_part)
        if keys[3]:
            self.angle = self.angle + self.angle_vel
            x_part = math.cos(2 * math.pi * self.angle / 360)
            y_part = math.sin(2 * math.pi * self.angle / 360)
            self.direction = (x_part, y_part)
        if keys[0]:
            px = self.position[0] + self.direction[0] * self.vel
            py = self.position[1] + self.direction[1] * self.vel
            self.position = (px, py)
        if keys[1]:
            px = self.position[0] - self.direction[0] * self.vel
            py = self.position[1] - self.direction[1] * self.vel
            self.position = (px, py)


if __name__ == '__main__':
    print("Please run racinggame.py as main.")
