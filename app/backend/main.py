from fastapi import FastAPI
from .api.endpoints import recipe

app = FastAPI()

app.include_router(recipe.router)

@app.get("/")
async def root():
    return {"hello": "world!"}