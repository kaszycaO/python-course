import numpy as np

def sigmoid(x):
    return 1.0/(1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1.0 - x)

def relu(x):
    return x * (x > 0)

def relu_derivative(x):
    return 1. * (x > 0)
