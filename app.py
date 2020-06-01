import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'Music_Library'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb+srv://root:r00tUser@cluster0-aveek.mongodb.net/Music_Library?retryWrites=true&w=majority')

mongo = PyMongo(app)


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html') 


@app.route('/all_genres')
def all_genres():
    return render_template('allgenres.html', genres=mongo.db.genre.find()) 
    

@app.route('/insert_genre', methods=['POST'])
def insert_genre():
    genre_doc = {'genre_name': request.form.get('genre_name')}
    mongo.db.genre.insert_one(genre_doc)
    return redirect(url_for('home'))


@app.route('/add_genre')
def add_genre():
    return render_template('addgenre.html')


@app.route('/edit_genre/<genre_id>')
def edit_genre(genre_id):
    return render_template('editgenre.html',
    genre=mongo.db.genre.find_one({'_id': ObjectId(genre_id)}))
 

@app.route('/update_genre/<genre_id>', methods=['POST'])
def update_genre(genre_id):
    mongo.db.genre.update(
        {'_id': ObjectId(genre_id)},
        {'genre_name': request.form.get('genre_name'),       
        'genre_image':request.form.get('genre_image'),})
    return redirect(url_for('home'))
   

@app.route('/delete_genre/<genre_id>')
def delete_genre(genre_id):
    mongo.db.genre.remove({'_id': ObjectId(genre_id)})
    return redirect(url_for('home'))


@app.route('/get_country')
def get_country():
    return render_template('country.html',
                           country=mongo.db.genre.find({"genre_name":"Country"}))


@app.route('/get_chill')
def get_chill():
    return render_template('chill.html',
                           chill=mongo.db.genre.find({"genre_name":"Chill"}))


@app.route('/get_folk')
def get_folkl():
    return render_template('folk.html',
                           folk=mongo.db.genre.find({"genre_name":"Folk"}))
    
    
@app.route('/get_songs')
def get_songs():
    return render_template("allsongs.html", 
                           songs=mongo.db.songs.find())
    

@app.route('/add_song')
def add_song():
    return render_template('addsong.html',
                           genres=mongo.db.genre.find())   
    
    
@app.route("/show_song/<song_id>")
def show_song(song_id):
    the_song = mongo.db.songs.find_one({"_id": ObjectId(song_id)})
    all_genres = mongo.db.genres.find()
    return render_template('showsong.html', song=the_song, genres=all_genres)


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


@app.route('/update_song/<song_id>', methods=["POST"])
def update_song(song_id):
    songs = mongo.db.songs
    songs.update( {'_id': ObjectId(song_id)},
    {
        'genre_name':request.form.get('genre_name'),
        'song_image':request.form.get('song_image'),
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
            port=int(os.environ.get('PORT', 3000)),
            debug=True)