import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from models import Base 

load_dotenv()

# de completat cu url ul real din .env
DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)