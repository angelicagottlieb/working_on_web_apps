
# {{ NAME }} Route Design Recipe

_Copy this design recipe template to test-drive a plain-text Flask route._

## 1. Design the Route Signature

_Include the HTTP method, the path, and any query or body parameters._

```
# Albums route

# Home route
POST /albums

```

## 2. Create Examples as Tests

_Go through each route and write down one or more example responses._

_Remember to try out different parameter values._

_Include the status code and the response body._

```python
# EXAMPLE

# POST /albums
#  Expected response (200 OK):
"""
New album successfully added.
"""

# GET /albums
#  Expected response (200 OK):
"""
List of records as string
"""

```

## 3. Test-drive the Route

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
"""
POST /albums
  Expected response (200 OK):
  "New album successfully added!"
"""
def test_new_album_successfully_created(web_client, db_connection):
    db_connection.seed('seeds/albums_table.sql')
    response = web_client.post('/albums', data={'title': 'Tortured Poets Society', 'release_year': 2024, 'artist_id': 3})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'New album successfully added!'
    response = web_client.get('/albums')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Album(1, 'Doolittle', 1989, 1), Album(2, Surfer Rosa', 1988, 1), Album(3, Waterloo', 1974, 2), Album(4, Super Trouper', 1980, 2), Album(5, Bossanova', 1990, 1), Album(6, Lover', 2019, 3), Album(7, Folklore', 2020, 3), Album(8, I Put a Spell on You', 1965, 4), Album(9, Baltimore', 1978, 4), Album(10, Here Comes the Sun', 1971, 4), Album(11, Fodder on My Wings', 1982, 4), Album(12, Ring Ring', 1973, 2), Album(13, Tortured Poets Society, 2024, 3)"

def test_get_albums(web_client, db_connection):
    db_connection.seed('seeds/albums_table.sql')
    response = web_client.get('/albums')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Album(1, 'Doolittle', 1989, 1), Album(2, Surfer Rosa', 1988, 1), Album(3, Waterloo', 1974, 2), Album(4, Super Trouper', 1980, 2), Album(5, Bossanova', 1990, 1), Album(6, Lover', 2019, 3), Album(7, Folklore', 2020, 3), Album(8, I Put a Spell on You', 1965, 4), Album(9, Baltimore', 1978, 4), Album(10, Here Comes the Sun', 1971, 4), Album(11, Fodder on My Wings', 1982, 4), Album(12, Ring Ring', 1973, 2)" 