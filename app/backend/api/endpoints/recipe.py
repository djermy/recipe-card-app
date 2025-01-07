from fastapi import APIRouter
from sqlmodel import Session
from backend.models.recipe import Recipe
from backend.database.db import db

router = APIRouter(
    prefix="/recipe",
    tags=["recipe"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def root():
    return {"explore": "popular recipes from other users"}

@router.post("/create")
async def create_recipe(recipe: Recipe):
    with Session(db.conn) as session:
        session.add(recipe) 
        session.commit()
   
    return {"message": "recipe created!"}