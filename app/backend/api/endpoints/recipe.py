from fastapi import APIRouter
from sqlmodel import Session, select
from backend.models.recipe import Recipe
from backend.database.store import store

router = APIRouter(
    prefix="/recipe",
    tags=["recipe"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def root():
    return store.recipe_store.get_all()

@router.get("/{recipe_id}")
async def get_recipe_by_id(id: int):
    return store.recipe_store.get(id)

@router.post("/create")
async def create_recipe(recipe: Recipe):
    return store.recipe_store.create(recipe)

@router.put("/update/{recipe_id}")
async def update_recipe(id: int, updated_recipe: Recipe):
    return store.recipe_store.update(id, updated_recipe)

@router.delete("/delete/{recipe_id}")
async def delete_recipe(id: int):
   return store.recipe_store.delete(id)