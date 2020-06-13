import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

from werkzeug.urls import url_encode, url_quote, url_join
from werkzeug.utils import redirect, format_string
from werkzeug.exceptions import HTTPException, NotFound, MethodNotAllowed, \
     BadHost
from werkzeug._internal import _get_environ, _encode_idna
from werkzeug._compat import itervalues, iteritems, to_unicode, to_bytes, \
    text_type, string_types, native_string_result, \
    implements_to_string, wsgi_decoding_dance
from werkzeug.datastructures import ImmutableDict, MultiDict

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'Music_Library'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb+srv://root:r00tUser@cluster0-aveek.mongodb.net/Music_Library?retryWrites=true&w=majority')

mongo = PyMongo(app)

    
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', 
                           genres=mongo.db.genre.find().sort("genre_name"))
    

@app.route('/get_country')
def get_country():
    return render_template('country.html', 
                           songs=mongo.db.songs.find({"genre_name":"Country"}).sort("artist_name"))
    

@app.route('/get_chill')
def get_chill():
    return render_template('chill.html', 
                           songs=mongo.db.songs.find({"genre_name":"Chill"}).sort("artist_name"))


@app.route('/get_folk')
def get_folk():
    return render_template('folk.html', 
                           songs=mongo.db.songs.find({"genre_name":"Folk"}).sort("artist_name"))


@app.route('/get_pop')
def get_pop():
    return render_template('pop.html', 
                           songs=mongo.db.songs.find({"genre_name":"Pop"}).sort("artist_name"))


@app.route('/get_rock')
def get_rock():
    return render_template('rock.html', 
                           songs=mongo.db.songs.find({"genre_name":"Rock"}).sort("artist_name"))
 

@app.route('/get_reggae')
def get_reggae():
    return render_template('reggae.html', 
                           songs=mongo.db.songs.find({"genre_name":"Reggae"}).sort("artist_name"))


@app.route('/get_urban')
def get_urban():
    return render_template('urban.html', 
                           songs=mongo.db.songs.find({"genre_name":"Urban"}).sort("artist_name"))


@app.route('/get_other')
def get_other():
    return render_template('other.html', 
                           songs=mongo.db.songs.find({"genre_name":"Other"}).sort("artist_name"))
              
    
@app.route('/get_songs')
def get_songs():
    return render_template('allsongs.html', 
                           songs=mongo.db.songs.find().sort("artist_name"), 
                           genres=mongo.db.genre.find())

 
@app.route("/show_song/<song_id>")
def show_song(song_id):
    the_song = mongo.db.songs.find_one({"_id": ObjectId(song_id)})
    all_genres = mongo.db.genre.find()
    return render_template('showsong.html', song=the_song, genres=all_genres)
    

@app.route('/add_song')
def add_song():
    return render_template('addsong.html',
                           song=mongo.db.songs.find(),
                           genres=mongo.db.genre.find())   


@app.route('/edit_song/<song_id>', methods=['POST'])
def edit_song(song_id):
    the_song =  mongo.db.songs.find_one({"_id": ObjectId(song_id)})
    all_genres =  mongo.db.genre.find()
    return render_template('editsongs.html', song=the_song, genres=all_genres)


@app.route('/insert_song', methods=['POST'])
def insert_song():
    songs =  mongo.db.songs
    songs.insert_one(request.form.to_dict())
    return redirect(url_for('get_songs'))


@app.route('/update_song/<song_id>', methods=['POST'])
def update_song(song_id):
    songs = mongo.db.songs
    songs.update( 
    {'_id': ObjectId(song_id)},
    {
        'genre_name':request.form.get('genre_name'),
        'song_image':request.form.get('song_image'),
        'album_name':request.form.get('album_name'),
        'song_name':request.form.get('song_name'),
        'artist_name':request.form.get('artist_name'),
        'song_link':request.form.get('song_link'),
    })
    return redirect(url_for('get_songs'))


@app.route('/delete_song/<song_id>', methods=['POST'])
def delete_song(song_id):
    mongo.db.songs.remove({'_id': ObjectId(song_id)})
    return redirect(url_for('get_songs'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('$PORT', 3000)),
            debug=True)