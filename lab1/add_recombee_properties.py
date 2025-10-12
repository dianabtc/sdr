from recombee_api_client.api_requests import AddItemProperty
from __init__ import client

spotify_properties = {
    "artists": "set",
    "album_name": "string",
    "track_name": "string",
    "popularity": "double",
    "duration_ms": "double",
    "explicit": "boolean",
    "danceability": "double",
    "energy": "double",
    "key": "int",
    "loudness": "double",
    "mode": "int",
    "speechiness": "double",
    "acousticness": "double",
    "instrumentalness": "double",
    "liveness": "double",
    "valence": "double",
    "tempo": "double",
    "time_signature": "int",
    "track_genre": "string"
}

def add_recombee_properties():
    for property, type in spotify_properties.items():
        client.send(AddItemProperty(property, type))

if __name__ == "__main__":
    add_recombee_properties()