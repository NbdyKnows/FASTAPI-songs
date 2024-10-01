from fastapi import FastAPI
from routes.songs import song

app = FastAPI(
    title="TICS",
    description="GRUPO 4"
)

app.include_router(song)

