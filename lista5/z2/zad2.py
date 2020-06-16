#!/usr/bin/env python3

import pandas as pd

import numpy as np

import matplotlib.pyplot as plt

def read_data():
    """Function used to read data from 'ratings.csv'"""

    read_ratings = pd.read_csv('ratings.csv', usecols= ['userId','movieId', 'rating'])
    data = read_ratings[read_ratings['movieId'] < 10000].to_numpy()

    max_user_id = int(max((data.T)[0]))
    max_movies_id = int(max((data.T)[1]))

    X = np.zeros((max_user_id, max_movies_id))
    previousId = 0
    counter = -1
    # preparation of matrix X
    for i in range(len(data)):
        check = int(data[i][0])
        # sort by user
        if check != previousId:
            counter += 1

        index = int(data[i][1]) - 1
        X[counter][index] = data[i][2]
        previousId = check

    return X

def cosine_similarity(x, y):

    f = np.nan_to_num
    normalized_matrix = f(x/np.linalg.norm(x, axis=0))
    similarity = np.dot(normalized_matrix, f(y/np.linalg.norm(y)))
    profile = f(similarity/np.linalg.norm(similarity))

    result = np.dot(normalized_matrix.T, profile)

    return result

def my_profile(length):
    """ Prepare own profile """

    # Film ids from movies.csv
    my_ratings = np.zeros((length, 1))
    # id = 2571
    my_ratings[2570] = 5
    # id = 32
    my_ratings[31] = 4
    # id = 260
    my_ratings[259] = 5
    # id = 1097
    my_ratings[1096] = 4

    return my_ratings

def print_data(result, films_to_recommend):
    """Function used to print results"""
    preparation = []
    read_movies = pd.read_csv('movies.csv', usecols= ['movieId', 'title'])

    #making a tuple (result, film_id)
    for i in range(len(result)):
        preparation.append((result[i][0], i))

    #sorting the tuple
    result_sorted = sorted(preparation, key=lambda x: x[0], reverse=True)

    for i in range(films_to_recommend):
        result = result_sorted[i][0]
        movie_id = result_sorted[i][1] + 1
        movie_name = read_movies[read_movies['movieId'] == movie_id].to_numpy()
        print(result, movie_name[0][1])

def main():

    np.seterr(all='ignore')

    x = read_data()
    y = my_profile(len(x[0]))
    result = cosine_similarity(x, y)
    print_data(result, 20)

if __name__ == "__main__":
    main()
