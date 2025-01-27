from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api.endpoints import recipe
from .models.recipe import Recipe
from .database.store import store

app = FastAPI()

origins = [
    "http://127.0.0.1:5500",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(recipe.router)

@app.on_event("startup")
def on_startup():
    store.create_db_and_tables()

@app.get("/")
async def root():
    return {"hello": "world"}