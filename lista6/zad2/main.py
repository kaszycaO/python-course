#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
from time import sleep

import neural_networks as mynn
import tools as t

def simulate(i, x_test, y_test):

    if i % 100 == 0:
        plt.clf()
        plt.title("Simulation, step: {}".format(i))

        plt.scatter(x_test, y_test)

        plt.draw()
        plt.pause(0.001)

def main():
    type = "square"
    
    if type == "square":
        X = np.linspace(-50, 50, 26)

        y = np.array([[z**2] for z in X ])
        x = np.array([[z, 1.0] for z in X ])

        X_test = np.linspace(-50, 50, 101)
        x_test = np.array([[z, 1.0] for z in X_test])

        nn = mynn.NeuralNetworkSquare(x, y)
        simulation = True
        for i in range(100000):

            nn.feedforward()
            nn.backprop()

            if simulation:
                simulate(i, X_test, nn.predict(x_test))

        if simulation == False:
            plt.title("Comparision")
            plt.scatter(X_test, X_test**2, label="Original")
            plt.scatter(X_test, nn.predict(x_test), label="Predicted")
            plt.legend()
            plt.show()

    elif type == "sin":
        x = np.linspace(0, 2, 21).reshape(21, 1)
        y = np.sin((3*np.pi/2) * x)
        x_test = np.linspace(0, 2, 161).reshape(161, 1)

        nn = mynn.NeuralNetworkSin(x, y)
        simulation = True
        for i in range(100000):

            nn.feedforward()
            nn.backprop()

            if simulation:
                simulate(i, x_test, nn.predict(x_test))

        if simulation == False:
            plt.title("Comparision")
            plt.scatter(x_test, np.sin((3*np.pi/2) * x_test), label="Original")
            plt.scatter(x_test, nn.predict(x_test), label="Predicted")
            plt.legend()
            plt.show()


if __name__ == "__main__":
    main()
