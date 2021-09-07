"""
Movie Recommender : 
1) main page :
    - get user input of 3 movie names and 3 scores
    - press submit button lead to recommender page
2) recommender page : 
    - return top10 recommended movies 
3) recommendation algorithms : 
    - DONE : nmf
    - TOTRY : PCA + clustering 
    - TOTRY : neighborhood-based collaborative filtering
"""

from flask import Flask, render_template, request
from jjx_movie_rec_app.nmf_recommender import recommend
import jjx_movie_rec_app.constants

app = Flask(__name__)

@app.route('/')
def index():
    movie_list = jjx_movie_rec_app.constants.MOVIE_LIST
    return render_template('main.html', movie_list=movie_list)

@app.route('/recommender')
def recommender_nmf():
    # get user input from browser
    movie1 = request.args.get('movie1', ' ')  # uses HTTP GET
    movie2 = request.args.get('movie2', ' ')  # retrieves variables from the URL
    movie3 = request.args.get('movie3', ' ') 
    score1 = request.args.get('score1', ' ')  # uses HTTP GET
    score2 = request.args.get('score2', ' ')  # retrieves variables from the URL
    score3 = request.args.get('score3', ' ') 
    # into dictionary format
    user_input = {
        movie1 : score1,
        movie2 : score2,
        movie3 : score3
    }
    # get recommendation from nmf_recommender
    top10 = recommend(user_input)
    # return to the recommender page on browser
    return render_template('nmf_recommender.html', movies=top10)


if __name__ == "__main__":
    app.run(debug=True, port=5000)