from fastapi import FastAPI
from .api.endpoints import recipe
from .models.recipe import Recipe
from .database.db import db

app = FastAPI()

app.include_router(recipe.router)

@app.on_event("startup")
def on_startup():
    db.create_db_and_tables()

@app.get("/")
async def root():
    return {"hello": "world"}