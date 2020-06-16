import numpy as np

class NeuralNetwork:

    def __init__(self, x, y, eta, functions, specialization, seed=17):
        np.random.seed(seed)

        self.specialization = specialization
        self.func1 = functions[0]
        self.deriv1 = functions[1]
        self.func2 = functions[2]
        self.deriv2 = functions[3]

        self.input = x
        self.weights1 = np.random.rand(4, self.input.shape[1])
        self.weights2 = np.random.rand(1, 4)
        self.y = y
        self.output = np.zeros(self.y.shape)
        self.eta = eta

    def feedforward(self):
        # first layer's output
        self.layer1 = self.func1(np.dot(self.input, self.weights1.T))

        # second layer's output
        self.output = self.func2(np.dot(self.layer1, self.weights2.T))

    def backprop(self):
        # hidden -> output
        delta2 = (self.y - self.output) * self.deriv2(self.output)
        d_weights2 = self.eta * np.dot(delta2.T, self.layer1)

        # input -> hidden
        delta1 = self.deriv1(self.layer1) * np.dot(delta2, self.weights2)
        d_weights1 = self.eta * np.dot(delta1.T, self.input)

        self.weights1 += d_weights1
        self.weights2 += d_weights2

    def learn(self):
        for i in range(5000):
            self.feedforward()
            self.backprop()
        self.print_results()


    def print_results(self):
        np.set_printoptions(precision=3, suppress=True)

        print("---------------------------------------------------------------")
        print("Neural Network with {} in hidden layer and {} in output layer".\
                format(self.func1.__name__, self.func2.__name__))

        print("Specialization in", self.specialization)
        print("NN         ORIGINAL")
        for i in range(self.output.shape[0]):
            spaces = (" ")*(12 - (len(str(self.output[i]))))
            print("{}{}{}".format(self.output[i], spaces, self.y[i]))

        print("")
        print("Weights (I and II)")
        print(self.weights1)
        print(self.weights2)
