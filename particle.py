from ray import Ray
import pygame
import math


WHITE = (255, 255, 255)


class Particle:

    def __init__(self, x, y, beams):
        self.position = (x, y)
        self.rays = []
        for i in range(beams):
            self.rays.append(Ray(x, y, 360 * i / beams))

    def position_at(self, pos):
        self.position = pos
        for ray in self.rays:
            ray.position_at(pos)

    def show(self, gs):
        for ray in self.rays:
            ray.show(gs)

    def cast(self, gs, walls):
        for ray in self.rays:
            closest_dist = math.inf
            closest_point = False
            for wall in walls:
                point = ray.cast(wall)
                if point:
                    dist = math.sqrt((point[0] - self.position[0])**2
                                     + (point[1] - self.position[1])**2)
                    if dist < closest_dist:
                        closest_dist = dist
                        closest_point = point
            if closest_point:
                pygame.draw.line(gs, WHITE, self.position, closest_point)


if __name__ == '__main__':
    print("Please run raycasting.py as main.")
