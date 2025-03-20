import os
from dotenv import load_dotenv
import pandas as pd
import requests

load_dotenv()

API_KEY = os.getenv('LASTFM_API_KEY')

df = pd.read_csv("C:/Users/ahmed/Downloads/iHateYouJulian/archive/fantano_ratings.csv")
# Function to fetch top 5 tags from Last.fm
def get_album_tags(artist, album):
    if album != "self-titled":
        url = f"https://ws.audioscrobbler.com/2.0/?method=album.gettoptags&api_key={API_KEY}&artist={artist}&album={album}&format=json"
    else:
        url = f"https://ws.audioscrobbler.com/2.0/?method=album.gettoptags&api_key={API_KEY}&artist={artist}&album={artist}&format=json"
    
    
    try:
        response = requests.get(url)
        data = (response.json())['toptags']['tag'][0:5]
        tag_list = [entry['name'] for entry in data]
        
        return ", ".join(tag_list) if tag_list else "unknown"
    
    except Exception as e:
        print(f"Error fetching tags for {album} by {artist}: {e}")
        return "unknown"

# Add tags to dataset lets gooo lamba function mentioned RAHHHHHHHHHHHHHHH
df["tags"] = df.apply(lambda row: get_album_tags(row["artist"], row["project_name"]), axis=1)

df = df.loc[df["tags"] != "unknown"]
df.to_csv("fantano_ratings_with_tags.csv", index=False)