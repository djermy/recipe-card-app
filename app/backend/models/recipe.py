from pydantic import BaseModel

class Recipe(BaseModel):
    name: str
    cook_time_hrs: float
    difficulty: str 
    rating: float | None = 0 
    likes: int | None = 0
    description: str