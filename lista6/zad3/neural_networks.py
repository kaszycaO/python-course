import numpy as np
import matplotlib.pyplot as plt

import tools as t

class NeuralNetworkSquare:

    def __init__(self, x, y):
        np.random.seed(17)
        self.input = x
        self.y = y
        self.weights1 = np.random.rand(40, self.input.shape[1])
        self.weights2 = np.random.rand(40, 40)
        self.weights3 = np.random.rand(1, 40)
        self.output = np.zeros(self.y.shape[0])
        self.eta = 0.00000001

    def feedforward(self):

        self.layer1 = t.sigmoid(np.dot(self.input, self.weights1.T))
        self.layer2 = t.relu(np.dot(self.layer1, self.weights2.T))
        self.output = t.relu(np.dot(self.layer2, self.weights3.T))

    def backprop(self):

        delta3 = (self.y - self.output) * t.relu_derivative(self.output)
        d_weights3 = self.eta * np.dot(delta3.T, self.layer2)
        delta2 = t.relu_derivative(self.layer2) * np.dot(delta3, self.weights3)
        d_weights2 = self.eta * np.dot(delta2.T, self.layer1)
        delta1 = t.sigmoid_derivative(self.layer1) * np.dot(delta2, self.weights2)
        d_weights1 = self.eta * np.dot(delta1.T, self.input)

        self.weights1 += d_weights1
        self.weights2 += d_weights2
        self.weights3 += d_weights3

    def predict(self, input):
        pred_1 = t.sigmoid(np.dot(input, self.weights1.T))
        pred_2 = t.relu(np.dot(pred_1, self.weights2.T))
        return t.relu(np.dot(pred_2, self.weights3.T))


class NeuralNetworkSin:

    def __init__(self, x, y):
        np.random.seed(13)

        self.input = x
        self.y = y
        self.weights1 = np.random.rand(15, self.input.shape[1])
        self.weights2 = np.random.rand(15, 15)
        self.weights3 = np.random.rand(1, 15)
        self.output = np.zeros(self.y.shape[0])
        self.eta = 0.005

    def feedforward(self):
        self.layer1 = t.tanh(np.dot(self.input, self.weights1.T))
        self.layer2 = t.tanh(np.dot(self.layer1, self.weights2.T))
        self.output = t.tanh(np.dot(self.layer2, self.weights3.T))

    def backprop(self):

        delta3 = (self.y - self.output) * t.tanh_derivative(self.output)
        d_weights3 = self.eta * np.dot(delta3.T, self.layer2)
        delta2 = t.tanh_derivative(self.layer2) * np.dot(delta3, self.weights3)
        d_weights2 = self.eta * np.dot(delta2.T, self.layer1)
        delta1 = t.tanh_derivative(self.layer1) * np.dot(delta2, self.weights2)
        d_weights1 = self.eta * np.dot(delta1.T, self.input)

        self.weights1 += d_weights1
        self.weights2 += d_weights2
        self.weights3 += d_weights3


    def predict(self, input):
        pred_1 = t.tanh(np.dot(input, self.weights1.T))
        pred_2 = t.tanh(np.dot(pred_1, self.weights2.T))
        return t.tanh(np.dot(pred_2, self.weights3.T))
