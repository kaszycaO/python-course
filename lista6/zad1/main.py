#!/usr/bin/env python3
import numpy as np

import neural_networks as mynn
import tools as t


def learning():
    type = "XOR"
    nrs_seed = 15
    ns_eta = 0.01

    # extra '1', in each column of X array is called bias unit, which allows to shift
    # the activation function. It's aproximation of function's constant term

    if type == "XOR":
        X = np.array([[0,0,1], [0,1,1], [1,0,1], [1,1,1]])
        Y = np.array([[0],[1],[1],[0]])

    elif type == "OR":
        X = np.array([[0,0,1], [0,1,1], [1,0,1], [1,1,1]])
        Y = np.array([[0],[1],[1],[1]])
        nrs_seed = 13
        ns_eta = 0.08

    elif type == "AND":
        X = np.array([[0,0,1], [0,1,1], [1,0,1], [1,1,1]])
        Y = np.array([[0],[0],[0],[1]])

    else:
        return


    # Universal parameters are not the best options, but learning results
    # are correct for each dataset (XOR, OR, AND)


    # just relu
    # universal seed = 17
    # universal eta = 0.01
    # best OR: eta = 0.08, seed =17
    params = [t.relu, t.relu_derivative, t.relu, t.relu_derivative]
    nr = mynn.NeuralNetwork(X, Y, ns_eta, params, type, seed=17)
    nr.learn()

    # just sigmoid
    # universal seed = 17
    # universal eta = 0.5
    params = [t.sigmoid, t.sigmoid_derivative, t.sigmoid, t.sigmoid_derivative]
    ns = mynn.NeuralNetwork(X, Y, 0.5, params, type)
    ns.learn()

    # first relu then sigmoid
    # best OR seed = 13 eta = 0.5
    # best XOR seed = 15 eta = 0.1
    # best AND seed = 15 eta = 0.1
    params = [t.relu, t.relu_derivative, t.sigmoid, t.sigmoid_derivative]
    nrs = mynn.NeuralNetwork(X, Y, 0.1, params, type, seed=nrs_seed)
    nrs.learn()

    # firs sigmoid then relu
    # universal seed = 20
    # universal eta = 0.1
    params = [t.sigmoid, t.sigmoid_derivative, t.relu, t.relu_derivative]
    nsr = mynn.NeuralNetwork(X, Y, 0.1, params, type, seed=20)
    nsr.learn()

if __name__ == "__main__":
    learning()
