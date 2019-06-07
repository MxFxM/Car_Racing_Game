import numpy as np
import random
import math


class Brain:
    def __init__(self):
        self.keyweights = np.array([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0],
                                    [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
        self.randomize()

    def randomize(self):
        kw = []
        for _ in range(4):
            w = []
            for _ in range(5):
                w.append(random.random()*2 - 1)
            kw.append(w)
        self.keyweights = np.array(kw)
        # random weights first

    def sigmoid(self, x):
        try:
            return 1/(1 + math.exp(-x))
        except Exception as e:
            print(f"Error: {e} \nwith x={x}")
        return 0

    def predict(self, sensor_inputs):
        keys = []
        for weights in self.keyweights:  # 4 keys
            keys.append(np.dot(sensor_inputs, weights))
        retkeys = []
        for k in keys:
            test = round(self.sigmoid(k))
            if test <= 0:
                retkeys.append(0)
            else:
                retkeys.append(test)
        return retkeys

    def clone(self):
        newbrain = Brain()
        for i in range(len(self.keyweights)):
            for j in range(len(self.keyweights[i])):
                newbrain.keyweights[i][j] = self.keyweights[i][j]
        return newbrain

    def mutate(self):
        mutation_rate = 0.15
        for i in range(len(self.keyweights)):
            for j in range(len(self.keyweights[i])):
                rand = random.random()
                if rand < mutation_rate:
                    self.keyweights[i][j] = random.random()


if __name__ == '__main__':
    print("Please run racinggame.py as main.")
