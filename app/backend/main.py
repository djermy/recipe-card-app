from fastapi import FastAPI
from .api.endpoints import recipe
from .models.recipe import Recipe
from .database.db import db

db.create_db_and_tables()

app = FastAPI()

app.include_router(recipe.router)

@app.get("/")
async def root():
    return {"hello": "world"}