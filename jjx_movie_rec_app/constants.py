""" constants used in application.py """

import os
import pandas as pd

PWD = os.getcwd()
RATINGS = pd.read_csv(f'{PWD}/ml-latest-small/ratings.csv')
MOVIES = pd.read_csv(f'{PWD}/ml-latest-small/movies.csv')
MOVIE_LIST = MOVIES['title'].to_list()


