from recombee_api_client.api_requests import AddUserProperty, SetUserValues
from __init__ import client
import csv

user_properties = {
    "age": "int",
    "gender": "string",
    "country": "string",
    "favorite_genres": "set",
    "premium": "boolean",
    "avg_listening_time": "double",
    "mood_preference": "string",
    "first_name": "string",
    "last_name": "string",
    "email": "string"
}

def add_user_properties():
    for property, type in user_properties.items():
        client.send(AddUserProperty(property, type))

def add_users_from_csv(csv_file_path):
    with open(csv_file_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            user_id = row["user_id"]
            props = {
                "first_name": row["first_name"],
                "last_name": row["last_name"],
                "email": row["email"],
                "age": int(row["age"]),
                "gender": row["gender"],
                "country": row["country"],
                "favorite_genres": row["favorite_genres"].split(';') if ';' in row["favorite_genres"] else [row["favorite_genres"]],
                "premium": row["premium"].lower() == "true",
                "avg_listening_time": float(row["avg_listening_time"]),
                "mood_preference": row["mood_preference"]
            }

            client.send(SetUserValues(user_id, props, cascade_create=True))

if __name__ == "__main__":
    add_user_properties()
    add_users_from_csv("../spotify_users.csv")