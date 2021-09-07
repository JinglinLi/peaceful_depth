"""get user movie rating and return movie recommendations according to nmf"""

import os
import random
import numpy as np
import pandas as pd
from sklearn.decomposition import NMF
from joblib import load

PWD = os.getcwd()

def recommend(user_input):
    # load fited nmf
    nmf = load(f'{PWD}/jjx_movie_rec_app/nmf.joblib') 
    umr = pd.read_csv(f'{PWD}/jjx_movie_rec_app/umr.csv', index_col=[0]) 
    Q = nmf.components_

    # calculate predicted user movie rating
    user_rating = pd.DataFrame(user_input, index=['user'], columns=umr.columns) # user input to df
    user_rating.fillna(umr.mean(axis=0), inplace=True) # fillna
    p_user = nmf.transform(user_rating) # transform
    r_user = np.dot(p_user, Q) # multiply Q -> user movie scores

    # recommend random 10 from top 50
    top = pd.DataFrame(r_user, index=['user'], columns=umr.columns)
    top50 = np.array(top.T.reset_index().sort_values('user', ascending=False).head(50)['index'])
    random.shuffle(top50)
    return top50[:10]

if __name__ == '__main__':
    user_input = {'Shawshank Redemption, The (1994)': '5', 'she': '4', 'Matrix, The (1999)': '5'}
    recommends = recommend(user_input)

