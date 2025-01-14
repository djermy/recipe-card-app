from sqlmodel import Field, SQLModel

class Recipe(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    cook_time_mins: int = Field(index=True)
    difficulty: str = Field(index=True, max_length=50) 
    rating: float | None = Field(default=0.0, index=True) 
    likes: int | None = Field(default=0, index=True)
    ingredients: str = Field(max_length=500)
    description: str = Field(max_length=500)