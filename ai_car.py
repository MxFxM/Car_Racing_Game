from ray import Ray
from brain import Brain
import pygame
import math
import numpy as np


BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)


class AiCar:
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
        self.rays.append(Ray(self.position[0], self.position[1], 50))
        self.rays.append(Ray(self.position[0], self.position[1], 130))
        self.brain = Brain()
        self.dead = False
        self.stuck = False
        self.isBest = False
        self.score = 0

    def show(self, surface):
        pos = (round(self.position[0]), round(self.position[1]))
        if not self.dead and not self.stuck:
            if not self.isBest:
                pygame.draw.circle(surface, BLUE, pos, 5)
            else:
                pygame.draw.circle(surface, GREEN, pos, 5)
        else:
            pygame.draw.circle(surface, RED, pos, 5)

    def mydist(self, pos1, pos2):
        dist = math.sqrt((pos1[0]-pos2[0])**2+(pos1[1]-pos2[1])**2)
        if dist < 2:
            self.dead = True
        return dist

    def score_points(self, checkpoints):
        for ray in self.rays:
            closest_dist = math.inf
            closest_point = False
            # first checkpoint has value 1
            for s, wall in enumerate(checkpoints, 1):
                point = ray.cast(wall)
                if point:
                    dist = math.sqrt((point[0] - self.position[0])**2
                                     + (point[1] - self.position[1])**2)
                    if dist < closest_dist:
                        closest_dist = dist
                        closest_point = point
                    if dist < 5:
                        if self.score == s-1:
                            self.score = s

    def cast(self, gs, walls):
        distances = []
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
                distances.append(self.mydist(self.position, closest_point))
            else:
                distances.append(0)
        # print(np.array(distances))
        return np.array(distances)

    def debugKeys(self, keys):
        if keys[0] and keys[1]:  # up and down has no action
            keys[0] = 0
            keys[1] = 0
        if keys[2] and keys[3]:  # left and right has no action
            keys[2] = 0
            keys[3] = 0
        if keys == [0, 0, 0, 0]:
            self.stuck = True
        return keys

    def drive(self, dists):
        keys = self.brain.predict(dists)
        keys = self.debugKeys(keys)
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

    def createChild(self):
        child = AiCar(150, 190, 270)
        child.brain = self.brain.clone()
        return child


if __name__ == '__main__':
    print("Please run racinggame.py as main.")
