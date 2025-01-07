from fastapi import APIRouter
from sqlmodel import Session, select
from backend.models.recipe import Recipe
from backend.database.db import db

router = APIRouter(
    prefix="/recipe",
    tags=["recipe"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def root():
    with Session(db.conn) as session:
        query = select(Recipe)
        response = session.exec(query)
        recipes = []
        for recipe in response:
            recipes.append(recipe)

    return recipes

@router.post("/create")
async def create_recipe(recipe: Recipe):
    with Session(db.conn) as session:
        session.add(recipe) 
        session.commit()
   
    return {"message": "recipe created!"}