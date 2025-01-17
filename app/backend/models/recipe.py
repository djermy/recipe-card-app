from sqlmodel import Field, SQLModel

class Recipe(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    prep_time_mins: int
    cook_time_mins: int
    total_cook_time: int | None = Field(default=0, index=True)
    difficulty: str = Field(index=True, max_length=8) 
    rating: float | None = Field(default=0.0, index=True) 
    likes: int | None = Field(default=0, index=True)
    ingredients: str = Field(max_length=500)
    instructions: str = Field(max_length=500)