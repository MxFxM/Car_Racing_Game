from ai_car import AiCar
import numpy as np
import time
import random


class Population:
    def __init__(self, size, start_steps, step_size):
        self.cars = []
        self.size = size
        self.step = 0
        self.max_steps = start_steps
        self.stepsize = step_size
        self.fitnesssum = 0
        self.generation = 1
        self.bestCar = 0
        for _ in range(size):
            self.cars.append(AiCar(150, 190, 270))

    def show(self, gs):
        for car in self.cars:
            car.show(gs)

    def update(self, gs, walls, checkpoints):
        for car in self.cars:
            if not car.dead and not car.stuck:
                distances = car.cast(gs, walls)
                distances = np.array(distances)
                car.drive(distances)
                car.score_points(checkpoints)
        self.step = self.step + 1

    def done(self):
        if self.step > self.max_steps:
            return True
        for car in self.cars:
            if not car.dead and not car.stuck:
                return False
        return True

    def calculatefitness(self):
        """
        -------------------------------------------------------------------
        vllt den score hier quadrieren damit besser seutlich besser wird
        wenn dann bei select parent beachten
        gemacht (hoch 3)
        """
        self.fitnesssum = 0
        for car in self.cars:
            self.fitnesssum = self.fitnesssum + car.score**3

    def selection(self):
        newcars = []
        self.setBestCar()
        newcars.append(self.cars[self.bestCar].createChild())
        newcars[0].isBest = True
        for _ in range(self.size - 6):  # 5 cars get made new
            parent = self.selectParent()
            newcars.append(parent.createChild())
        self.cars = newcars
        for _ in range(5):
            self.cars.append(AiCar(150, 190, 270))  # 5 random cars
        print(f"Generation {self.generation} done @ {time.time()}")
        print(f"{len(self.cars)} cars alive")
        self.generation = self.generation + 1
        self.step = 0
        self.max_steps = self.max_steps + self.stepsize

    def mutation(self):
        for car in self.cars[1:]:  # dont change the previous best
            car.brain.mutate()

    def setBestCar(self):
        best = 0
        best_index = 0
        for i, car in enumerate(self.cars):  # starts at 0
            if car.score > best:
                best = car.score
                best_index = i
        self.bestCar = best_index
        print(f"Best score: {best} from Car No.{best_index}")

    def selectParent(self):
        rand = random.random() * self.fitnesssum
        runningsum = 0
        for car in self.cars:
            runningsum = runningsum + car.score**3
            if runningsum >= rand:
                return car
        # should not be here
        print("Error when selecting parents. Returning first one (randomly).")
        return self.cars[0]


if __name__ == '__main__':
    print("Please run racinggame.py as main.")
