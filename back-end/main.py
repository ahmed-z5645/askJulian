from typing import Union

from fastapi import FastAPI

app = FastAPI()

#cant beleive this is the only api end point for now lol
@app.get("/albums/getRating/{artist}/{album}")
def get_rating(artist: str, album: str):
    #first, we need to get the tags of the album, then process tags, and then predict rating, and send to front end
    return
