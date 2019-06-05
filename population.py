from ai_car import AiCar
import numpy as np


class Population:
    def __init__(self, size):
        self.cars = []
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


if __name__ == '__main__':
    print("Please run racinggame.py as main.")
