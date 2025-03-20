import requests
import os
from dotenv import load_dotenv

def getInfo(artist, album):
    API_KEY = os.getenv('LASTFM_API_KEY')
    infoURL = f"https://ws.audioscrobbler.com/2.0/?method=album.getinfo&api_key={API_KEY}&artist={artist}&album={album}&format=json"
    tagURL = f"https://ws.audioscrobbler.com/2.0/?method=album.gettoptags&api_key={API_KEY}&artist={artist}&album={album}&format=json"
    
    try:
        infoRes = requests.get(infoURL)
        infoData = infoRes.json()
        tagRes = requests.get(tagURL)
        tagData = infoRes.json()
        
        infoArray = []
        print(infoData)
        tagData = (tagRes.json())['toptags']['tag'][0:5]

        return tagData
    except Exception as e:
        print(f"Error fetching tags for {album} by {artist}: {e}")
        return "unknown"
    
getInfo("tyler, the creator", "igor")