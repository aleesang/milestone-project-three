import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'Music_Library'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb+srv://root:r00tUser@cluster0-aveek.mongodb.net/Music_Library?retryWrites=true&w=majority')

mongo = PyMongo(app)


@app.route('/')
@app.route('/get_songs')
def get_songs():
    return render_template("songs.html", 
                           tasks=mongo.db.songs.find())


@app.route('/get_genres')
def get_genres():
    return render_template('genres.html',
                           genres=mongo.db.genre.find())

@app.route('/add_song')
def add_song():
    return render_template('addsong.html',
                           categories=mongo.db.genre.find())

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)