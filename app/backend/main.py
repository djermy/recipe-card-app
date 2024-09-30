from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Recipe(BaseModel):
    name: str
    ingredients: str
    prep_time: int | float
    beginner_friendly: bool

@app.get("/")
def read_root():
    return {"hello": "world!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q" : q}

@app.put("/recipes/{recipe_id}")
def update_recipe(recipe_id: int, recipe: Recipe):
    return {
        "recipe_name": recipe.name,
        "ingredients": recipe.ingredients,
        "prep_time": recipe.prep_time,
        "beginner_friendly": recipe.beginner_friendly
    }