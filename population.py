from ai_car import AiCar
import numpy as np


class Population:
    def __init__(self, size, start_steps, step_size):
        self.cars = []
        self.size = size
        self.step = 0
        self.max_steps = start_steps
        self.stepsize = step_size
        for _ in range(size):
            self.cars.append(AiCar(150, 190, 270))

    def show(self, gs):
        for car in self.cars:
            car.show(gs)

    def update(self, gs, walls):
        for car in self.cars:
            if not car.dead and not car.stuck:
                distances = car.cast(gs, walls)
                distances = np.array(distances)
                car.drive(distances)
        self.step = self.step + 1

    def done(self):
        if self.step > self.max_steps:
            return True
        for car in self.cars:
            if not car.dead and not car.stuck:
                return False
        return True

    def selection(self):
        self.cars = []
        for _ in range(self.size):
            self.cars.append(AiCar(150, 190, 270))

    def creation(self):
        self.step = 0
        self.max_steps = self.max_steps + self.stepsize


if __name__ == '__main__':
    print("Please run racinggame.py as main.")
