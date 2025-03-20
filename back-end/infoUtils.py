import requests
import os
from dotenv import load_dotenv

load_dotenv()
def getLastFMInfo(artist, album):
    API_KEY = os.getenv('LASTFM_API_KEY')
    
    infoURL = f"https://ws.audioscrobbler.com/2.0/?method=album.getinfo&api_key={API_KEY}&artist={artist}&album={album}&format=json"
    tagURL = f"https://ws.audioscrobbler.com/2.0/?method=album.gettoptags&api_key={API_KEY}&artist={artist}&album={album}&format=json"
    
    try:
        infoRes = requests.get(infoURL)
        infoData = infoRes.json()
        tagRes = requests.get(tagURL)
        tagData = infoRes.json()
        
        infoArray = []
        infoArray.append(infoData['album']['image'][2]['#text'])
        infoArray.append(getYear(artist, album))
        tagData = (tagRes.json())['toptags']['tag'][0:5]
        tagData = [entry['name'] for entry in tagData]
        infoArray.append(", ".join(tagData) if tagData else "unknown")
        return infoArray
    except Exception as e:
        print(f"Error fetching tags for {album} by {artist}: {e}")
        return "unknown"
    
def getYear(artist, album):
    
    
    DISCOGS_API_KEY= os.getenv("DISCOGS_API_KEY")
    url = f"https://api.discogs.com/database/search?release_title={album}&artist={artist}&per_page=1&page=1&token={DISCOGS_API_KEY}"
    try:
        response = requests.get(url)
        data = (response.json())['results'][0]['year']
        return data

    except Exception as e:
        print(f"Error getting year of release for {album} by {artist}: {e}")
        return "unknown"