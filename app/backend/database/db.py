import os
from dotenv import load_dotenv
from sqlmodel import create_engine

load_dotenv()

class Database:
    def __init__(self, db_url):
        self.db_url = os.getenv("DB_URL")
        self.conn = create_engine(db_url)