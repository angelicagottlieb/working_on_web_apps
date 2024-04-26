from lib.database_connection import get_flask_database_connection
from lib.album_repository import AlbumRepository
from lib.album import Album
from lib.artist import *
from lib.artist_repository import ArtistRepository
from flask import request


def apply_example_music_app(app):
    @app.route('/albums', methods=['POST'])
    def create_new_album():
        connection = get_flask_database_connection(app)
        repository = AlbumRepository(connection)
        title = request.form['title']
        release_year = request.form['release_year']
        artist_id = request.form['artist_id']
        album = Album(None, title, release_year, artist_id)
        repository.create(album)
        return "New album successfully added!"
    
    @app.route('/albums', methods=['GET'])
    def get_albums():
        connection = get_flask_database_connection(app)
        repository = AlbumRepository(connection)
        albums = repository.all()
        response = ''
        for i, album in enumerate(albums):
            response += f"{album}"
            if i < len(albums) - 1:
                response += ", "
        return response
    
    @app.route('/artists', methods=['GET'])
    def get_artists():
        connection = get_flask_database_connection(app)
        repository = ArtistRepository(connection)
        artists = repository.all()
        response = ''
        for i, artist in enumerate(artists):
            response += f"{artist}"
            if i < len(artists) - 1:
                response += ", "
        return response
    
    @app.route('/artists', methods=['POST'])
    def create_new_artist():
        connection = get_flask_database_connection(app)
        repository = ArtistRepository(connection)
        name = request.form['name']
        genre = request.form['genre']
        artist = Artist(None, name, genre)
        repository.create(artist)
        return "New artist successfully added!"
    
    