from flask import request, jsonify
from imdb import app
from imdb.models import Movie


@app.before_request
def before_request_callback():
    auth = request.authorization
    if auth.username != 'admin' or auth.password != '1234':
        return jsonify({'Error': 'Unauthorised access'})


@app.route("/search", methods=['GET', 'POST'])
def search():

    #keyword = request.args.get('keyword')
    #keyword = request.get_data()
    keyword = request.get_json()['keyword']
    if keyword:
        movies = Movie.query.filter((Movie.name.like('%' + keyword + '%'))
                                | (Movie.production.like('%' + keyword + '%'))
                                | (Movie.genre.like('%' + keyword + '%'))
                                | (Movie.year.like('%' + keyword + '%')))
    else:
        movies = Movie.query.all()

    output = []
    for movie in movies:
        data={}
        data['name'] = movie.name
        data['production'] = movie.production
        data['genre'] = movie.genre
        data['popularity'] = movie.popularity
        data['year'] = movie.year
        output.append(data)

    return jsonify({'movies': output})


@app.route('/')
def api_hub():
    return 'Welcome to Api-hub!'