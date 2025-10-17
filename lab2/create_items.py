from recombee_api_client.api_requests import Batch, SetItemValues
import csv
from __init__ import client

def add_items_from_csv(csv_file_path, batch_size=100):
    with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        batch = []

        for i, row in enumerate(reader, start=1):
            item_id = row["track_id"]
            properties = {
                "artists": row["artists"].split(';') if ';' in row["artists"] else [row["artists"]],
                "album_name": row["album_name"],
                "track_name": row["track_name"],
                "popularity": float(row["popularity"]),
                "duration_ms": float(row["duration_ms"]),
                "explicit": row["explicit"].lower() == "true",
                "danceability": float(row["danceability"]),
                "energy": float(row["energy"]),
                "key": int(row["key"]),
                "loudness": float(row["loudness"]),
                "mode": int(row["mode"]),
                "speechiness": float(row["speechiness"]),
                "acousticness": float(row["acousticness"]),
                "instrumentalness": float(row["instrumentalness"]),
                "liveness": float(row["liveness"]),
                "valence": float(row["valence"]),
                "tempo": float(row["tempo"]),
                "time_signature": int(row["time_signature"]),
                "track_genre": row["track_genre"],
            }

            batch.append(SetItemValues(item_id, properties, cascade_create=True))

            if len(batch) == batch_size:
                client.send(Batch(batch))
                batch = []

        if batch:
            client.send(Batch(batch))

if __name__ == "__main__":
    add_items_from_csv("../spotify_dataset.csv")
