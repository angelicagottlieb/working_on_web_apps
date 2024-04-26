import os 
from lib.database_connection import get_flask_database_connection
from lib.album_repository import *
from lib.album import *
from flask import Flask, request




def test_new_album_successfully_created(web_client, db_connection):
    db_connection.seed('seeds/albums_table.sql')
    response = web_client.post('/albums', data={'title': 'Tortured Poets Society', 'release_year': 2024, 'artist_id': 3})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'New album successfully added!'
    response = web_client.get('/albums')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Album(1, Doolittle, 1989, 1), Album(2, Surfer Rosa, 1988, 1), Album(3, Waterloo, 1974, 2), Album(4, Super Trouper, 1980, 2), Album(5, Bossanova, 1990, 1), Album(6, Lover, 2019, 3), Album(7, Folklore, 2020, 3), Album(8, I Put a Spell on You, 1965, 4), Album(9, Baltimore, 1978, 4), Album(10, Here Comes the Sun, 1971, 4), Album(11, Fodder on My Wings, 1982, 4), Album(12, Ring Ring, 1973, 2), Album(13, Tortured Poets Society, 2024, 3)"

def test_get_albums(web_client, db_connection):
    db_connection.seed('seeds/albums_table.sql')
    response = web_client.get('/albums')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Album(1, Doolittle, 1989, 1), Album(2, Surfer Rosa, 1988, 1), Album(3, Waterloo, 1974, 2), Album(4, Super Trouper, 1980, 2), Album(5, Bossanova, 1990, 1), Album(6, Lover, 2019, 3), Album(7, Folklore, 2020, 3), Album(8, I Put a Spell on You, 1965, 4), Album(9, Baltimore, 1978, 4), Album(10, Here Comes the Sun, 1971, 4), Album(11, Fodder on My Wings, 1982, 4), Album(12, Ring Ring, 1973, 2)" 

def test_get_artists(web_client, db_connection):
    db_connection.seed('seeds/albums_table.sql')
    response = web_client.get('/artists')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Artist(1, Pixies, Rock), Artist(2, ABBA, Pop), Artist(3, Taylor Swift, Pop), Artist(4, Nina Simone, Jazz)"

def test_new_artist_successfully_created(web_client, db_connection):
    db_connection.seed('seeds/albums_table.sql')
    response = web_client.post('/artists', data={'name': 'Wild nothing', 'genre': 'Indie'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "New artist successfully added!"
    response = web_client.get('/artists')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Artist(1, Pixies, Rock), Artist(2, ABBA, Pop), Artist(3, Taylor Swift, Pop), Artist(4, Nina Simone, Jazz), Artist(5, Wild nothing, Indie)"