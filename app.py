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
                           songs=mongo.db.songs.find())
    

@app.route('/add_song')
def add_song():
    return render_template('addsong.html',
                           genre=mongo.db.genre.find())   
    
    
@app.route('/edit_song/<song_id>')
def edit_song(song_id):
    the_song =  mongo.db.songs.find_one({"_id": ObjectId(song_id)})
    all_genre =  mongo.db.genre.find()
    return render_template('editsongs.html', song=the_song,
                           genre=all_genre)


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
        'song_name':request.form.get('song_name'),
        'genre_name':request.form.get('genre_name'),
    })
    return redirect(url_for('get_songs'))


@app.route('/delete_song/<song_id>')
def delete_song(song_id):
    mongo.db.songs.remove({'_id': ObjectId(song_id)})
    return redirect(url_for('get_songs'))


@app.route('/get_genres')
def get_genres():
    return render_template('genres.html',
                           genres=mongo.db.genre.find())


@app.route('/insert_genre', methods=['POST'])
def insert_genre():
    genre_doc = {'genre_name': request.form.get('genre_name')}
    mongo.db.genre.insert_one(genre_doc)
    return redirect(url_for('get_genres'))


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
        {'genre_name': request.form.get('genre_name')})
    return redirect(url_for('get_genres'))
   

@app.route('/delete_genre/<genre_id>')
def delete_genre(genre_id):
    mongo.db.genre.remove({'_id': ObjectId(genre_id)})
    return redirect(url_for('get_genres'))
 

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT', 3000)),
            debug=True)
