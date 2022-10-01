from flask import Flask, jsonify, request
import csv
import random

app = Flask(__name__)
allmovies = []
with open('D:/Code/Py/venv/movies.csv', encoding='utf-8') as f:
    reader = csv.reader(f)
    data = list(reader)
    allmovies = data[1:]

likedmovies = []
dislikedmovies = []
unwatchedmovies = []


@app.route('/api', methods=['GET'])
def api():
    return jsonify({'data': allmovies[:20], 'status': 'ok'})


@app.route('/api/liked', methods=['POST'])
def lm():
    global allmovies
    i = random.randint(0, len(allmovies))
    movie = allmovies[i]
    allmovies.pop(i)
    likedmovies.append(movie)
    return jsonify({'likedmovie': likedmovies[len(likedmovies) - 1], 'status': 'ok'})


@app.route('/api/disliked', methods=['POST'])
def dlm():
    global allmovies
    i = random.randint(0, len(allmovies))
    movie = allmovies[i]
    allmovies.pop(i)
    dislikedmovies.append(movie)
    return jsonify({'dislikedmovie': dislikedmovies[len(dislikedmovies) - 1], 'status': 'ok'})

@app.route('/api/unwatched', methods=['POST'])
def uwm():
    global allmovies
    i = random.randint(0, len(allmovies))
    movie = allmovies[i]
    allmovies.pop(i)
    unwatchedmovies.append(movie)
    return jsonify({'unwatchedmovie': unwatchedmovies[len(unwatchedmovies) - 1], 'status': 'ok'})

@app.route('/api/all/liked', methods=['GET'])
def al():
    return jsonify({'likedmovies': likedmovies[:20], 'status': 'ok'})

@app.route('/api/all/disliked', methods=['GET'])
def adl():
    return jsonify({'dislikedmovies': dislikedmovies[:20], 'status': 'ok'})

@app.route('/api/all/unwatched', methods=['GET'])
def au():
    return jsonify({'unwatchedmovies': unwatchedmovies[:20], 'status': 'ok'})

@app.route('/api/all', methods=['GET'])
def a():
    return jsonify({'likedmovies': likedmovies[:20], 'dislikedmovies': dislikedmovies[:20], 'unwatchedmovies': unwatchedmovies[:20], 'status': 'ok'})

if __name__ == '__main__':
    app.run()
