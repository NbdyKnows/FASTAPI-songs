from typing import Optional
from pydantic import BaseModel

class Song(BaseModel):
    id: Optional[str] = None
    name: str
    artist: str
    album: str
    year: int