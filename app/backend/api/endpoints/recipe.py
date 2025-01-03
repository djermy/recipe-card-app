from fastapi import APIRouter
from backend.models.recipe import Recipe

router = APIRouter(
    prefix="/recipe",
    tags=["recipe"],
    responses={404: {"description": "Not found"}},
)

@router.post("/create")
async def create_recipe(recipe: Recipe):
    return recipe