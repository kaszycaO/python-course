#!/usr/bin/env python3

import pandas as pd

import numpy as np

from sklearn.linear_model import LinearRegression

import matplotlib.pyplot as plt


def read_data(filename, n):
    in_file = pd.read_csv(filename, usecols= ['userId', 'movieId', 'rating'])

    Y = in_file.rating[in_file['movieId'] == 1.0].to_numpy()
    Y = np.array([[el] for el in Y])

    data = in_file[in_file['movieId'] < n].to_numpy()

    X = np.zeros((len(Y), n))
    goodId = -1
    counter = -1
    for i in range(len(data)):
        check = int(data[i][1])
        if check == 1:
            goodId = int(data[i][0])
            counter += 1
        elif goodId == data[i][0]:
            X[counter][check - 2] = data[i][2]

    return X, Y

def predict(X, Y):
    """ Linear Regression """

    training_set = X[:200]
    training_values = Y[:200]

    test_set = X[200:]
    test_values = Y[200:]

    model = LinearRegression()
    model.fit(training_set, training_values)
    result = model.score(training_set, training_values)
    print("Accuracy on training_set: ", result)

    y_pred = model.predict(X)
    comparation = pd.DataFrame({'Actual': test_values.flatten(), 'Predicted' :
                                y_pred[200:].flatten()})
    print(comparation)

def regression(X, Y):
    """Function used to show regression line """

    x = np.sum(X, axis=1)
    A = np.vstack([x, np.ones(len(x))]).T
    a, c = np.linalg.lstsq(A,Y, rcond=None)[0]

    _ = plt.plot(x, Y, 'o', label ='Original data')
    _ = plt.plot(x, x*a + c, 'r', label ='Regression line')
    _ = plt.legend()
    plt.show(block=False)

def main():

    try:
        m = input("m: ").strip()
        m = int(m)
    except ValueError:
        print("Invalid character! Integer needed!")
        return

    X, Y = read_data("ratings.csv", m)
    regression(X, Y)
    predict(X, Y)
    plt.show()

if __name__ == "__main__":
    main()
