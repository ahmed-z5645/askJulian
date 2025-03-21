from typing import Union
from infoUtils import getLastFMInfo
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import tensorflow as tf
import pickle
import numpy as np

app = FastAPI()
model = tf.keras.models.load_model("C:/Users/ahmed/Downloads/iHateYouJulian/askJulian/back-end/julian.h5")
model.compile(optimizer="adam", loss="mean_squared_error")

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])
# Load label encoders once
with open("C:/Users/ahmed/Downloads/iHateYouJulian/askJulian/back-end/label_encoders.pkl", "rb") as f:
    label_encoders = pickle.load(f)

album_mapping = {name: idx for idx, name in enumerate(label_encoders["album"].classes_)}
artist_mapping = {name: idx for idx, name in enumerate(label_encoders["artist"].classes_)}

def encode_album_name(album_name):
    return album_mapping.get(album_name, -1)

def encode_artist(artist):
    return artist_mapping.get(artist, -1)

def mlb_tags(tags):
    all_classes = np.concatenate([label_encoders["tags"].classes_, np.unique(tags)])  # Combine known and new tags
    label_encoders["tags"].classes_ = np.unique(all_classes)  # Update MLB classes_
    return label_encoders["tags"].transform([tags])[0]

#cant beleive this is the only api end point for now lol
@app.get("/albums/getRating")
def get_rating(artist: str, album: str):
    artist = artist.lower()
    album = album.lower()
    image, year, tags = getLastFMInfo(artist, album)
    
    try:
        album_encoded = encode_album_name(album)
        artist_encoded = encode_artist(artist)
        tags_list = tags.split(",") 
        padded_tags = np.pad(tags_list[:5], (0, 5 - len(tags_list)), mode="constant", constant_values=0)
        tags_encoded = mlb_tags(padded_tags)

        input_data = [np.array([[album_encoded]]), np.array([[artist_encoded]]), np.array([[int(year)]]), np.array([tags_encoded])]
        
        prediction = model.predict(input_data)[0][0]
        return {"predicted_rating": round(float(prediction), 2),
                "image": image,
                "year": year,
                "artist": artist,
                "album": album}

    except Exception as e:
        print("error:", str(e))
        return {"error": str(e)}

