""" fit and save nmf model """

import os
import pandas as pd
from sklearn.decomposition import NMF
from joblib import dump

PWD = os.getcwd()
# read data
ratings = pd.read_csv(f'{PWD}/ml-latest-small/ratings.csv')
movies = pd.read_csv(f'{PWD}/ml-latest-small/movies.csv')

# generate rating matrix and save to csv
user_movie_rating = ratings[['userId', 'movieId', 'rating']].pivot(index='userId', columns='movieId')
user_movie_rating.columns = user_movie_rating.columns.droplevel() # droplevel of multileveled column name
umr = pd.DataFrame(columns=movies['movieId'].values) # get movie titles
umr = umr.append(user_movie_rating)
umr.columns = movies['title'].values
umr.fillna(2.5, inplace=True)
umr.to_csv(f'{PWD}/jjx_movie_rec_app/umr.csv')

# instanciate and fit nmf and save fit nmf
nmf = NMF(n_components=20, max_iter=1000)
nmf.fit(umr)
dump(nmf, f'{PWD}/jjx_movie_rec_app/nmf.joblib')

