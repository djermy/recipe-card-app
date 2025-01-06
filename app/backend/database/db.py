import os
from dotenv import load_dotenv
from sqlmodel import SQLModel, create_engine

load_dotenv()

class Database:
    def __init__(self):
        self.db_url = os.getenv("DB_URL")
        self.conn = create_engine(self.db_url, echo=True)
    
    def create_db_and_tables(self):
        SQLModel.metadata.create_all(self.conn)

db = Database()