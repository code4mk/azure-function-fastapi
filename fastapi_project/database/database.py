from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

SQLALCHEMY_DATABASE_URL = os.getenv('DATABASE_URL')

# Create the SQLAlchemy engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create a session maker bound to the engine
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Declarative base class for database models
Base = declarative_base()