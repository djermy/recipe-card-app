from fastapi import APIRouter, Depends, HTTPException
from ...dependencies import get_token_header
from backend.models.recipe import Recipe

router = APIRouter(
    prefix="/recipe",
    tags=["recipe"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

@router.post("/create")
def create_recipe(recipe: Recipe):
    return recipe