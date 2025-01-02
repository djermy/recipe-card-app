from fastapi import Depends, FastAPI
from .dependencies import get_query_token, get_token_header
from .api.endpoints import recipe

app = FastAPI(
    dependencies=[Depends(get_query_token)]
)

app.include_router(recipe.router)

@app.get("/")
def root():
    return {"hello": "world!"}