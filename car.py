from ray import Ray
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
        self.vel = 3
        self.angle_vel = 3
        self.rays = []
        self.rays.append(Ray(self.position[0], self.position[1], 270))
        self.rays.append(Ray(self.position[0], self.position[1], 300))
        self.rays.append(Ray(self.position[0], self.position[1], 240))
        self.rays.append(Ray(self.position[0], self.position[1], 0))
        self.rays.append(Ray(self.position[0], self.position[1], 180))
        self.rays.append(Ray(self.position[0], self.position[1], 70))
        self.rays.append(Ray(self.position[0], self.position[1], 110))

    def show(self, surface):
        pos = (round(self.position[0]), round(self.position[1]))
        pygame.draw.circle(surface, BLUE, pos, 5)

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
                pygame.draw.line(gs, BLUE, self.position, closest_point)

    def update(self, keys):
        oa = self.angle
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
        for ray in self.rays:
            ray.position_at(self.position)
            ray.update_angle(self.angle - oa)


if __name__ == '__main__':
    print("Please run racinggame.py as main.")
