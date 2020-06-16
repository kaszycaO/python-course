#!/usr/bin/env python3

import pandas as pd

import numpy as np

import matplotlib.pyplot as plt

from scipy.sparse import lil_matrix
from scipy.sparse.linalg import norm


def read_data():
    """Function used to read data from 'ratings.csv'"""

    read_ratings = pd.read_csv('ratings.csv', usecols= ['userId','movieId', 'rating'])
    data = lil_matrix(read_ratings)


    max_user_id = max(read_ratings.userId.to_numpy())
    max_movies_id = max(read_ratings.movieId.to_numpy())

    X = lil_matrix((max_user_id, max_movies_id))
    previousId = 0
    counter = -1

    # preparation of matrix X
    for i in range(data.shape[0]):
        check = int(data[i, 0])
        # sort by user
        if check != previousId:
            counter += 1

        index = int(data[i, 1]) - 1
        X[counter, index] = data[i, 2]
        previousId = check

    return X

def cosine_similarity(x, y):

    np.seterr(all='ignore')

    f = np.nan_to_num
    normalized_matrix = lil_matrix(f(x/norm(x, axis=0)))
    similarity = normalized_matrix.dot(f(y/norm(y)))
    profile = f(similarity/norm(similarity))
    result = f((normalized_matrix.transpose()).dot(profile))

    return result

def my_profile(length):
    """ Prepare own profile """
    
    
    # Film ids from movies.csv
    my_ratings = lil_matrix((length, 1))
    # id = 79132
    my_ratings[79131] = 3
    # id = 60069
    my_ratings[60068] = 4
    # id = 109487
    my_ratings[109486] = 5
    # id = 122886
    my_ratings[122885] = 4
    # id = 122887
    my_ratings[168251] = 2

    return my_ratings

def print_data(result, films_to_recommend):
    """Function used to print results"""
    preparation = []
    read_movies = pd.read_csv('movies.csv', usecols= ['movieId', 'title'])

    # making a tuple (result, film_id)
    for i in range(result.shape[0]):
        preparation.append((result[i,0], i))


    #sorting the tuple
    result_sorted = sorted(preparation, key=lambda x: x[0], reverse=True)

    print()
    print("Recommended films: ")
    print()
    for i in range(films_to_recommend):
        result = result_sorted[i][0]
        movie_id = result_sorted[i][1] + 1
        movie_name = read_movies[read_movies['movieId'] == movie_id].to_numpy()
        # movie_name[0] for names with id
        print(result, movie_name[0][1])

def main():
    print("Reading data ...")
    x = read_data()
    y = my_profile(x.shape[1])
    print("Data has been read! Prediction in progress ... ")
    result = cosine_similarity(x, y)
    print("Prediction complete! Preparing data to display ... ")
    print_data(result, 20)

if __name__ == "__main__":
    main()
