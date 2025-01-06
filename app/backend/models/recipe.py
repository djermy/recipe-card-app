from sqlmodel import Field, SQLModel

class Recipe(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    cook_time_hrs: float = Field(index=True)
    difficulty: str = Field(index=True) 
    rating: float | None = Field(default=0.0, index=True) 
    likes: int | None = Field(default=0, index=True)
    description: str