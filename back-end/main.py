from typing import Union
from infoUtils import getLastFMInfo
from fastapi import FastAPI
import tensorflow as tf
import pickle
import numpy as np

app = FastAPI()
model = tf.keras.models.load_model("C:/Users/ahmed/Downloads/iHateYouJulian/askJulian/back-end/julian.h5")
model.compile(optimizer="adam", loss="mean_squared_error")

print(model.loss)
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
@app.get("/albums/getRating/{artist}/{album}")
def get_rating(artist: str, album: str):
    image, year, tags = getLastFMInfo(artist, album)
    
    try:
        print("here")
        album_encoded = encode_album_name(album)
        artist_encoded = encode_artist(artist)
        tags_list = tags.split(",") 
        padded_tags = np.pad(tags_list[:5], (0, 5 - len(tags_list)), mode="constant", constant_values=0)
        tags_encoded = mlb_tags(padded_tags)

        input_data = [np.array([[album_encoded]]), np.array([[artist_encoded]]), np.array([[int(year)]]), np.array([tags_encoded])]
        
        prediction = model.predict(input_data)[0][0]
        print(prediction)
        return {"predicted_rating": round(prediction, 1)}

    except Exception as e:
        print("error:", str(e))
        return {"error": str(e)}
    
get_rating("tyler, the creator", "igor")

