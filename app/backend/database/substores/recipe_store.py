from backend.models.recipe import Recipe
from sqlmodel import Session, select

class Recipe_Store:
    def __init__(self, conn):
        self.conn = conn

    def get(self, recipe):
        pass
    
    def get_all(self):
        with Session(self.conn) as session:
            query = select(Recipe)
            response = session.exec(query)
            recipes = []
            for recipe in response:
                recipes.append(recipe)

        return recipes

    def create(self, recipe: Recipe):
        with Session(self.conn) as session:
            session.add(recipe) 
            session.commit()
            session.refresh(recipe)

        return [{"message": "recipe created!"}, recipe.dict()]