from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine
from app.models import Base
from app.routers import game, users

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["X-User-Data"],
)

Base.metadata.create_all(bind=engine)

@app.get("/")
def greet():
    return { "message": "Hi from backend wordle"}

app.include_router(game.router, tags=["wordle"])
app.include_router(users.router, tags=["users"])