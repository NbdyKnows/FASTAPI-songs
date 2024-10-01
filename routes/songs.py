from fastapi import APIRouter, HTTPException
from config.db import conn
from models.song import songs
from schemas.song import Song

song = APIRouter()

@song.get("/songs")
def get_songs():
    return conn.execute(songs.select()).mappings().all()


@song.post("/song/create")
def create_songs(song: Song):
    new_song = {"name": song.name, "artist": song.artist, "album": song.album, "year": song.year}
    
    add = conn.execute(songs.insert().values(new_song))
    conn.commit() 
    
    return conn.execute(songs.select().where(songs.c.id == add.lastrowid)).mappings().first()


@song.get("/song/search/{id}")
def read_song(id: str):
    result = conn.execute(songs.select().where(songs.c.id == id)).mappings().first()
    
    if result:
        return dict(result)
    return "Error: Canción no encontrada"


@song.put("/song/update/{id}")
def update_song(id: str, song: Song):
    conn.execute(songs.update()
                .values(name=song.name, artist=song.artist, album=song.album, year=song.year)
                .where(songs.c.id==id))
    
    conn.commit()
    return conn.execute(songs.select().where(songs.c.id == id)).mappings().first()


@song.delete("/song/delete/{id}")
def delete_song(id: str):
    conn.execute(songs.delete().where(songs.c.id == id))
    conn.commit()
    return "Eliminado"